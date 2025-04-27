from dotenv import load_dotenv
import os

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

    SQLALCHEMY_DATABASE_URI = f'mysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False