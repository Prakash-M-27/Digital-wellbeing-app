
# Digital Well-Being & Cognitive Fatigue Decision Bot

## Quick Start (5 minutes)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python app.py
```

### Step 3: Open Browser
Navigate to: `http://localhost:5000`

## Features Implemented ✓

### 1. User Digital Activity Profiling
- Track activities: study, work, social media, entertainment, breaks
- Automatic categorization and duration tracking

### 2. Screen Time Monitoring Dashboard
- Real-time display of total screen time
- Break frequency counter
- Activity breakdown by type
- Continuous usage hours tracker

### 3. Rule-Based Fatigue Detection
- Continuous usage detection (>2 hours)
- Late-night activity alerts (after 10 PM)
- Break deficiency detection
- Severity classification (high/medium/low)

### 4. Personalized Break & Wellness Recommendations
- Eye exercises (20-20-20 rule)
- Hydration reminders
- Stretching suggestions
- Context-aware recommendations based on fatigue level

### 5. Real-Time Usage Adjustment
- Dynamic fatigue level updates
- Continuous hours tracking
- State-aware break detection

### 6. AI-Based Cognitive Fatigue Prediction
- Behavioral analytics scoring (0-100)
- Weighted factors: total hours, breaks, late-night usage
- Predictive risk assessment

### 7. Decision Log & Explainability
- Complete audit trail of all decisions
- Timestamp tracking
- Human-readable explanations for every alert
- Risk and recommendation logging

### 8. Adaptive Workload Balance Advisor
- Daily screen time limit analysis
- Break frequency recommendations
- Late-night usage pattern detection
- Schedule adjustment suggestions

### 9. Natural Language Well-Being Assistant
- Chat interface for user queries
- Usage summaries on demand
- Wellness tips and advice
- Fatigue level inquiries
- Medical advice prohibition with clear explanations

### 10. Routine Conflict Resolver
- Unhealthy pattern identification
- Late-night usage detection
- Excessive screen time alerts
- Actionable improvement suggestions

## Safety Restrictions Implemented ✓

- ❌ No medical diagnosis or mental health treatment
- ❌ No real-time device control or screen locks
- ❌ No invasive data collection
- ✓ All recommendations include explanations
- ✓ No hard-coded responses (logic-driven)
- ✓ Simulated data only
- ✓ State-aware decision handling
- ✓ Explainable denial responses

## Usage Examples

### Log an Activity
1. Select activity type (study/work/social/entertainment/break)
2. Enter duration in minutes
3. Click "Log Activity"
4. View instant fatigue analysis and recommendations

### Chat with Assistant
- "Show me my usage summary"
- "Give me a wellness tip"
- "What's my fatigue level?"
- "I need a break suggestion"

### View Workload Analysis
- Click "Refresh Analysis" in Workload Balance Advisor
- Review detected issues and suggestions
- Follow schedule adjustment recommendations

## Architecture

```
app.py                  # Flask backend with all logic
├── Activity Tracking   # POST /api/activity
├── Dashboard API       # GET /api/dashboard
├── Chat Assistant      # POST /api/chat
├── Decision Logs       # GET /api/logs
└── Workload Advisor    # GET /api/workload

templates/
└── index.html         # Single-page dashboard UI
```

## Fatigue Scoring Algorithm

```python
score = (total_hours × 10) - (breaks × 5) + (late_night_activities × 15)
Range: 0-100
- 0-40: Normal (green)
- 41-70: Moderate (yellow)
- 71-100: High (red)
```

## Rules Configuration

```python
max_continuous_hours = 2
late_night_start = 22:00
early_morning_end = 06:00
min_break_minutes = 15
daily_screen_limit = 8 hours
```

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Storage**: In-memory (for demo)
- **ML**: Behavioral analytics scoring

## Future Enhancements

- Database persistence (SQLite/PostgreSQL)
- User authentication
- Historical trend analysis
- Export reports (PDF/CSV)
- Mobile responsive design
- Push notifications
- Integration with screen time APIs

## Troubleshooting

**Port already in use:**
```bash
python app.py
# Change port in app.py: app.run(port=5001)
```

**Module not found:**
```bash
pip install Flask
```

## License

MIT License - Free to use and modify
=======
# 🧠 Digital Well-Being & Cognitive Fatigue Bot

An intelligent web application that helps users maintain healthy digital habits by monitoring screen time, analyzing cognitive fatigue, and providing personalized wellness recommendations.

## 📌 Features

- 📊 Real-time Digital Well-Being Dashboard
- ⏱️ Screen Time Tracking
- 🧠 Cognitive Fatigue Risk Analysis
- ☕ Break Reminder System
- 🌙 Late Night Usage Detection
- 💬 AI Wellness Assistant
- 📋 Activity Logging
- 📈 Decision Logging
- 🎯 Personalized Recommendations
- 👁️ Eye Care & Productivity Tips

---

## 🚀 Technologies Used

- HTML5
- CSS3
- JavaScript (Vanilla)

---

## 📷 Project Preview

### Dashboard
- Track daily screen time
- Monitor fatigue level
- Count breaks taken

### Activity Logger
Users can log:
- Study
- Work
- Social Media
- Entertainment
- Break

along with:
- Duration
- Time of Day

---

## 🧠 Cognitive Fatigue Analysis

The application calculates fatigue based on:

- Continuous screen usage
- Total screen time
- Number of breaks
- Late-night sessions
- Break-to-work ratio

Risk Levels:

- 🟢 Low Risk
- 🟠 Moderate Risk
- 🔴 High Risk

---

## 💬 AI Well-Being Assistant

The chatbot can answer questions about:

- Usage Summary
- Break Recommendations
- Eye Care
- Sleep Tips
- Productivity
- Fatigue Analysis

The assistant intentionally avoids:

- Medical diagnosis
- Mental health treatment
- Device control

---

## 📋 Decision Log

The system records:

- Trigger event
- Decision taken
- Reasoning behind recommendation

This improves transparency of the recommendation engine.

---

## 📂 Project Structure

```
Digital-WellBeing-Bot/
│
├── index.html
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/yourusername/Digital-WellBeing-Bot.git
```

2. Open the project folder.

3. Double-click **index.html**

or

Open it using **Live Server** in Visual Studio Code.

---

## 📸 Screenshots

Add screenshots here after uploading them.

Example:

```
screenshots/dashboard.png
screenshots/chatbot.png
```

---

## 🔮 Future Improvements

- User Login System
- Firebase Integration
- Data Persistence
- Weekly Analytics
- Monthly Reports
- AI-powered Personalized Suggestions
- Mobile Responsive Design
- Dark Mode
- Notification Support

---

## 🎯 Learning Outcomes

This project demonstrates:

- Frontend Web Development
- DOM Manipulation
- State Management
- User Activity Tracking
- Rule-Based AI
- Cognitive Fatigue Analysis
- Human-Computer Interaction
- Digital Wellness Concepts

---

## 🤝 Contributing

Contributions are welcome.

Feel free to fork the repository and submit a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Prakash**

3rd Year Computer Science Engineering Student

SRM TRP Engineering College

GitHub: https://github.com/yourusername

