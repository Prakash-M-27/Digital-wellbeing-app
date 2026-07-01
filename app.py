from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
import json
import random

app = Flask(__name__)

# In-memory storage
user_activities = []
decision_logs = []
fatigue_state = {"level": 0, "last_break": None, "continuous_hours": 0}

# Rule-based thresholds
RULES = {
    "max_continuous_hours": 2,
    "late_night_start": 22,
    "early_morning_end": 6,
    "min_break_minutes": 15,
    "daily_screen_limit": 8
}

def calculate_fatigue_score(activities):
    """AI-based fatigue prediction using behavioral analytics"""
    if not activities:
        return 0
    
    total_hours = sum(a['duration'] for a in activities) / 60
    breaks = sum(1 for a in activities if a['type'] == 'break')
    late_night = sum(1 for a in activities if a.get('hour', 12) >= RULES['late_night_start'])
    
    # Weighted scoring
    score = (total_hours * 10) - (breaks * 5) + (late_night * 15)
    return min(max(score, 0), 100)

def detect_fatigue_risks(activity):
    """Rule-based fatigue detection"""
    risks = []
    
    # Continuous usage check
    if fatigue_state['continuous_hours'] >= RULES['max_continuous_hours']:
        risks.append({
            "type": "continuous_usage",
            "severity": "high",
            "reason": f"Continuous screen time of {fatigue_state['continuous_hours']} hours without break"
        })
    
    # Late night activity
    hour = activity.get('hour', datetime.now().hour)
    if hour >= RULES['late_night_start'] or hour <= RULES['early_morning_end']:
        risks.append({
            "type": "late_night",
            "severity": "medium",
            "reason": f"Activity detected at {hour}:00 - outside healthy hours"
        })
    
    # Lack of breaks
    if fatigue_state['last_break']:
        time_since_break = (datetime.now() - fatigue_state['last_break']).seconds / 3600
        if time_since_break > 2:
            risks.append({
                "type": "no_break",
                "severity": "medium",
                "reason": f"No break taken for {time_since_break:.1f} hours"
            })
    
    return risks

def generate_recommendations(risks, fatigue_score):
    """Personalized wellness recommendations"""
    recommendations = []
    
    if fatigue_score > 70:
        recommendations.append({
            "action": "Take immediate 20-minute break",
            "reason": f"High fatigue score ({fatigue_score}/100) detected",
            "tips": ["Close eyes for 20 seconds", "Look at distant objects", "Drink water"]
        })
    elif fatigue_score > 40:
        recommendations.append({
            "action": "Schedule 15-minute break soon",
            "reason": f"Moderate fatigue score ({fatigue_score}/100)",
            "tips": ["Stand and stretch", "Walk around", "Hydrate"]
        })
    
    for risk in risks:
        if risk['type'] == 'continuous_usage':
            recommendations.append({
                "action": "Apply 20-20-20 rule",
                "reason": risk['reason'],
                "tips": ["Every 20 min, look 20 feet away for 20 seconds"]
            })
        elif risk['type'] == 'late_night':
            recommendations.append({
                "action": "Wind down screen usage",
                "reason": risk['reason'],
                "tips": ["Enable blue light filter", "Prepare for sleep", "Avoid stimulating content"]
            })
        elif risk['type'] == 'no_break':
            recommendations.append({
                "action": "Take break now",
                "reason": risk['reason'],
                "tips": ["Eye exercises", "Neck rotation", "Deep breathing"]
            })
    
    return recommendations

def log_decision(activity, risks, recommendations, fatigue_score):
    """Maintain decision audit trail"""
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "activity": activity,
        "fatigue_score": fatigue_score,
        "risks_detected": risks,
        "recommendations": recommendations,
        "explanation": f"Analyzed {activity['type']} activity. Fatigue score: {fatigue_score}/100. Detected {len(risks)} risk(s)."
    }
    decision_logs.append(log_entry)
    return log_entry

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/activity', methods=['POST'])
def add_activity():
    """Log new activity"""
    data = request.json
    activity = {
        "type": data['type'],
        "duration": int(data['duration']),
        "timestamp": datetime.now().isoformat(),
        "hour": datetime.now().hour
    }
    
    user_activities.append(activity)
    
    # Update fatigue state
    if activity['type'] == 'break':
        fatigue_state['last_break'] = datetime.now()
        fatigue_state['continuous_hours'] = 0
    else:
        fatigue_state['continuous_hours'] += activity['duration'] / 60
    
    # Detect risks and generate recommendations
    risks = detect_fatigue_risks(activity)
    fatigue_score = calculate_fatigue_score(user_activities[-10:])
    recommendations = generate_recommendations(risks, fatigue_score)
    
    # Log decision
    log = log_decision(activity, risks, recommendations, fatigue_score)
    
    # Update fatigue level
    fatigue_state['level'] = fatigue_score
    
    return jsonify({
        "success": True,
        "fatigue_score": fatigue_score,
        "risks": risks,
        "recommendations": recommendations,
        "log": log
    })

@app.route('/api/dashboard')
def dashboard():
    """Get dashboard data"""
    total_screen_time = sum(a['duration'] for a in user_activities if a['type'] != 'break') / 60
    total_breaks = sum(1 for a in user_activities if a['type'] == 'break')
    
    # Activity breakdown
    activity_breakdown = {}
    for activity in user_activities:
        atype = activity['type']
        activity_breakdown[atype] = activity_breakdown.get(atype, 0) + activity['duration']
    
    return jsonify({
        "total_screen_time": round(total_screen_time, 2),
        "total_breaks": total_breaks,
        "fatigue_level": fatigue_state['level'],
        "continuous_hours": round(fatigue_state['continuous_hours'], 2),
        "activity_breakdown": activity_breakdown,
        "recent_activities": user_activities[-10:]
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    """Natural language assistant"""
    message = request.json.get('message', '').lower()
    
    # Prohibited requests
    if any(word in message for word in ['diagnose', 'depression', 'anxiety', 'mental health', 'treatment']):
        return jsonify({
            "response": "I cannot provide medical diagnosis or mental health treatment. I can only offer digital wellness suggestions. Please consult a healthcare professional for medical concerns.",
            "explanation": "Medical advice is outside my scope per safety restrictions."
        })
    
    # Handle queries
    if 'summary' in message or 'usage' in message:
        total_time = sum(a['duration'] for a in user_activities if a['type'] != 'break') / 60
        response = f"You've used screens for {total_time:.1f} hours today. Your current fatigue level is {fatigue_state['level']}/100."
    elif 'break' in message or 'rest' in message:
        response = "Take a 15-minute break: try eye exercises (look far away), stretch your body, drink water, and step away from screens."
    elif 'tip' in message or 'advice' in message:
        tips = [
            "Follow the 20-20-20 rule: every 20 minutes, look 20 feet away for 20 seconds.",
            "Take regular breaks every 2 hours to prevent cognitive fatigue.",
            "Avoid screens 1 hour before bedtime for better sleep quality.",
            "Stay hydrated - drink water every hour during screen time.",
            "Adjust screen brightness to match ambient lighting."
        ]
        response = random.choice(tips)
    elif 'fatigue' in message or 'tired' in message:
        response = f"Your fatigue score is {fatigue_state['level']}/100. " + (
            "High fatigue detected - take a break immediately!" if fatigue_state['level'] > 70
            else "Moderate fatigue - consider taking a break soon." if fatigue_state['level'] > 40
            else "Fatigue levels are normal. Keep taking regular breaks!"
        )
    else:
        response = "I can help with: usage summary, break suggestions, wellness tips, or fatigue assessment. What would you like to know?"
    
    return jsonify({
        "response": response,
        "explanation": "Generated based on your current activity patterns and wellness rules."
    })

@app.route('/api/logs')
def get_logs():
    """Get decision logs"""
    return jsonify({"logs": decision_logs[-20:]})

@app.route('/api/workload')
def workload_advisor():
    """Adaptive workload balance advisor"""
    if not user_activities:
        return jsonify({"advice": "No activity data yet. Start logging your activities!"})
    
    total_hours = sum(a['duration'] for a in user_activities if a['type'] != 'break') / 60
    breaks = sum(1 for a in user_activities if a['type'] == 'break')
    
    advice = []
    if total_hours > RULES['daily_screen_limit']:
        advice.append({
            "issue": "Excessive screen time",
            "suggestion": f"Reduce daily usage by {total_hours - RULES['daily_screen_limit']:.1f} hours",
            "reason": f"You've exceeded the recommended {RULES['daily_screen_limit']} hour daily limit"
        })
    
    if breaks < total_hours / 2:
        advice.append({
            "issue": "Insufficient breaks",
            "suggestion": f"Add {int(total_hours/2 - breaks)} more breaks to your routine",
            "reason": "Recommended: 1 break per 2 hours of screen time"
        })
    
    late_activities = [a for a in user_activities if a.get('hour', 12) >= RULES['late_night_start']]
    if late_activities:
        advice.append({
            "issue": "Late-night usage detected",
            "suggestion": "Shift activities to earlier hours (before 10 PM)",
            "reason": "Late-night screen exposure disrupts sleep quality"
        })
    
    return jsonify({"advice": advice if advice else [{"message": "Your workload balance looks healthy!"}]})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
