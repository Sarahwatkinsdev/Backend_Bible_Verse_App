import os

SECRET_KEY = os.getenv('SECRET_KEY')
# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"
BIBLE_API_KEY = "3b6e0af64bcccb01742365b8f62086e3"
CORS_ALLOWED_ORIGINS = "http://127.0.0.1:8080"