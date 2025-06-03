import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_HEADER_TYPE = 'JWT'

    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

    if ENVIRONMENT == "production":
        SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") 
    else:
        SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///data.db")

