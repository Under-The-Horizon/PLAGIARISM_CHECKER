import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY          = os.getenv('SECRET_KEY', 'fallback-secret')
    UPLOAD_FOLDER       = 'uploads'

    # Mail
    MAIL_SERVER         = 'smtp.gmail.com'
    MAIL_PORT           = 587
    MAIL_USE_TLS        = True
    MAIL_USERNAME       = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD       = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME')

    # Third-party API keys (used in services, not Flask config)
    GEMINI_API_KEY      = os.getenv('GEMINI_API_KEY')
    TAVILY_API_KEY      = os.getenv('TAVILY_API_KEY')