# PlagiarismGuard

A Flask-based plagiarism detection system using a dual-layer engine:
- **Gestalt pattern matching** for peer-to-peer side-by-side comparison
- **Winnowing (cryptographic hashing)** for O(1) global database scans
- **Semantic ML model** (MiniLM) for paraphrase detection
- **Tavily + Gemini AI** for internet plagiarism investigation

---

## Project Structure

```
PLAGIARISM_CHECKER/
├── app.py                      ← Entry point (create_app factory)
├── config.py                   ← All app settings, reads from .env
├── database.py                 ← SQLite schema + helper functions
├── winnowing_engine.py         ← Winnowing fingerprint algorithm
├── utils.py                    ← ML semantic similarity model
├── requirements.txt
├── .env                        ← Secrets (never commit this)
├── .gitignore
│
├── routes/
│   ├── __init__.py
│   ├── auth.py                 ← /login  /register  /logout  /confirm_email
│   ├── auth_helpers.py         ← User class for Flask-Login
│   ├── student.py              ← /student-portal  /upload  /join_course
│   ├── teacher.py              ← /teacher-portal  /grade  /create_course
│   └── compare.py              ← /compare  /global_winnow_scan  /inspect_global
│
├── services/
│   ├── __init__.py
│   ├── analysis.py             ← Text extraction + highlighting logic
│   ├── internet_scan.py        ← Tavily search + Gemini AI report
│   └── email_service.py        ← Verification email + token helpers
│
├── templates/                  ← Jinja2 HTML templates (unchanged)
├── static/                     ← CSS / JS / images (unchanged)
└── uploads/                    ← Student file uploads (auto-created)
```

---

## Setup

### 1. Clone and create a virtual environment
```bash
git clone <your-repo-url>
cd PLAGIARISM_CHECKER
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create your `.env` file
Create a file called `.env` in the project root:
```
SECRET_KEY=your-random-secret-key
MAIL_USERNAME=youremail@gmail.com
MAIL_PASSWORD=your-gmail-app-password
GEMINI_API_KEY=your-gemini-api-key
TAVILY_API_KEY=your-tavily-api-key
```

> **Gmail tip:** Use an [App Password](https://myaccount.google.com/apppasswords),
> not your real Gmail password. 2FA must be enabled on your account.

### 4. Run the server
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your browser.

---

## Database

SQLite (`database.db`) is created automatically on first run via `init_db()`.
Tables: `users`, `courses`, `enrollments`, `tasks`, `assignments`, `document_fingerprints`.

---

## How the dual-layer detection works

| Layer | Algorithm | Purpose |
|---|---|---|
| Peer-to-peer | Gestalt (difflib) | Exact structural copying, powers side-by-side highlighting |
| Global scan | Winnowing (MD5 hashing) | Fast O(1) lookup against entire submission history |
| Paraphrase | MiniLM cosine similarity | Catches reworded/paraphrased plagiarism |
| Internet | Tavily search + Gemini | Detects content copied from the web |

---

## Security notes

- `.env` is listed in `.gitignore` — never commit it.
- Passwords are hashed with Werkzeug's `generate_password_hash` (PBKDF2).
- Email verification tokens expire after 1 hour (itsdangerous).
- Foreign keys and `ON DELETE CASCADE` are enforced in SQLite.
