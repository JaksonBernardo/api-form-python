from dotenv import load_dotenv
import os
from datetime import timedelta

class Config:

    """Configuration class for the Flask application."""

    load_dotenv()

    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')
    DEBUG = os.getenv('DEBUG')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('PASSWORD')
    DB = os.getenv('DB')
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=2)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

    SQLALCHEMY_DATABASE_URI = f'mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False