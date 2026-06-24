# 🚀 Autofix MCP

AI-Powered Self-Healing Customer Service Microservice

## 📌 Project Overview

Autofix MCP is an AI-powered customer service microservice that can:

- Generate and detect application errors
- Log errors automatically
- Monitor logs using a scheduler
- Analyze errors using Google Gemini AI
- Generate bug fix suggestions
- Save AI-generated fixes
- Create Git commits automatically
- Integrate with GitHub MCP for repository actions

---

## 🏗️ Architecture

FastAPI Application
↓
Error Generated
↓
error.log
↓
Scheduler
↓
Gemini AI
↓
Fix Suggestion
↓
Git Commit
↓
GitHub MCP

---

## 📂 Project Structure

```text
Autofix MCP
│
├── ai
│   ├── fixer.py
│   └── fix_suggestion.txt
│
├── app
│   ├── main.py
│   ├── logger.py
│   ├── scheduler.py
│   └── logs
│       └── error.log
│
├── .env
├── .env.example
├── requirements.txt
└── README.md
```

## ⚙️ Features

### Customer Service API

- Add customers
- Retrieve customers
- Generate intentional application errors

### Error Monitoring

- Scheduler checks logs periodically
- Detects application failures automatically

### AI Error Analysis

- Reads source code
- Reads application logs
- Sends information to Gemini AI
- Generates fix suggestions

### GitHub MCP Integration

- Connects to GitHub using MCP
- Can create GitHub Issues
- Can create Pull Requests
- Can interact with repositories

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/molikarathore7/autofix-mcp.git
cd autofix-mcp
```

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run Application

Start FastAPI:

```bash
uvicorn app.main:app --reload --port 8001
```

Start Scheduler:

```bash
python app/scheduler.py
```

---

## 🧪 Test Error Detection

Open:

```text
http://127.0.0.1:8001/customer-email
```

This intentionally generates an error.

The scheduler will:

1. Detect the error
2. Run Gemini AI
3. Generate a fix suggestion
4. Save output to:

```text
ai/fix_suggestion.txt
```

---

## 🛠️ Technologies Used

- Python
- FastAPI
- Google Gemini AI
- Git
- GitHub MCP
- Schedule Library
- dotenv

---

## 👩‍💻 Author

Molika Rathore