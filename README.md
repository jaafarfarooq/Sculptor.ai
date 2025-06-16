# 🧠 Sculptor.ai

Sculptor.ai is a health-focused web application that calculates Total Daily Energy Expenditure (TDEE) and macronutrient breakdown based on user input. It includes:

- 🔐 User signup & login (JWT authentication)
- 🧮 TDEE Calculator (FastAPI backend)
- 📊 Interactive dashboard (Streamlit frontend)
- 📦 Modular architecture (ready for future features)

---

## ⚙️ Setup Instructions

### 📁 Clone the Repository

```bash
git clone https://github.com/jaafarfarooq/Sculptor.ai.git
cd Sculptor.ai
```

---

## 🐍 Create and Activate Virtual Environment

### ✅ On Windows (PowerShell):

```bash
python -m venv .venv
.venv\Scripts\activate
```

### ✅ On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 📦 Install Dependencies

Make sure your virtual environment is activated, then:

```bash
pip install -r requirements.txt
```

---

## 🚀 Run FastAPI Backend (API server)

```bash
uvicorn app.main:app --reload
```

By default, it runs at: [http://localhost:8000](http://localhost:8000)

---

## 🖥️ Run Streamlit Frontend (Dashboard UI)

```bash
streamlit run .\streamlit_app\app.py
```

Or on macOS/Linux:

```bash
streamlit run ./streamlit_app/app.py
```

---

## 📌 Project Structure

```
Sculptor.ai/
│
├── app/                     # FastAPI backend
│   ├── main.py              # Entry point for FastAPI
│   ├── models/              # SQLAlchemy models
│   ├── auth/                # Auth routes and logic
│   └── services/            # Business logic
│
├── streamlit_app/           # Frontend Streamlit UI
│   └── app.py               # Dashboard code
│
├── requirements.txt
└── README.md
```

---

## 🛡️ Authentication

- Sign up and login are handled via JWT tokens.
- The token must be sent with authenticated API requests using the `Authorization: Bearer <token>` header.

---

## 🧱 Future Features (Planned)
- Meal planner
- Progress tracking
- Nutrition history
- User profile & settings

---

## 🧑‍💻 Author

Jaafar Bin Farooq  
🔗 [GitHub Profile](https://github.com/jaafarfarooq)
