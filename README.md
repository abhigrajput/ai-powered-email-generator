# AI Powered Email Generator

An AI-powered Smart Email Drafting Assistant built using Generative AI, Flask, JavaScript, and NVIDIA NIM APIs.  
The application helps users generate professional, well-structured emails instantly using Large Language Models (LLMs).

---

# Features

- AI-generated professional emails
- Multiple email categories
- Tone selection support
- Copy generated emails
- Download generated emails
- Email history storage using SQLite
- Responsive modern UI
- Real-time AI response generation
- NVIDIA NIM API integration
- Flask backend architecture

---

# Tech Stack

## Frontend
- HTML
- CSS
- JavaScript

## Backend
- Python
- Flask

## Database
- SQLite
- SQLAlchemy

## AI & APIs
- NVIDIA NIM API
- Meta Llama 3.3 70B Instruct

---

# Project Structure

```bash
AI-Powered-Email-Generator/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
└── instance/
    └── emails.db
```

---

# Screenshots

## Home Page

Add your screenshot here.

```markdown
![Home Page](screenshots/home.png)
```

---

# How It Works

1. User enters email requirement
2. User selects email type and tone
3. Frontend sends request to Flask backend
4. Backend creates optimized AI prompt
5. NVIDIA NIM API processes request
6. LLM generates professional email
7. Generated email displayed on frontend
8. Email saved into SQLite database

---

# Installation

## Clone Repository

```bash
git clone https://github.com/abhigrajput/ai-powered-email-generator.git
```

---

## Move Into Project Folder

```bash
cd ai-powered-email-generator
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory.

```env
NVIDIA_API_KEY=your_api_key_here
```

---

# Run Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# Future Improvements

- User authentication system
- AI email reply generator
- Gmail integration
- Multi-language support
- Resume-to-email generation
- Professionalism score analyzer
- Cloud deployment
- React frontend upgrade

---

# Learning Outcomes

This project helped in understanding:

- Generative AI integration
- Prompt Engineering
- REST APIs
- Flask backend development
- Database integration
- Frontend-backend communication
- Full-stack application architecture

---

# License

This project is licensed under the MIT License.

---

# Author

## Abhishek Rajput

GitHub:
https://github.com/abhigrajput

---
