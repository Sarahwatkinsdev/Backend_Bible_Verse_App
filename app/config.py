import os

SECRET_KEY = os.getenv('SECRET_KEY')
# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"
