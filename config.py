# config.py
import os
import secrets
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(basedir, 'instance', 'database.db')

# Ensure the 'instance' folder exists
if not os.path.exists(os.path.join(basedir, 'instance')):
    os.makedirs(os.path.join(basedir, 'instance'))

# JWT_SECRET_KEY を固定値に設定
JWT_SECRET_KEY = 'bisdom20252HBXXXWGFIRSTTRIAL'
# JWT_SECRET_KEY = secrets.token_hex(32)
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=1)
JWT_COOKIE_HTTPONLY = True
JWT_TOKEN_LOCATION = ['headers', 'cookies']
JWT_COOKIE_SECURE = True
JWT_REFRESH_COOKIE_PATH ="/refresh"
# SQLiteデータベースのURI
SQLALCHEMY_DATABASE_URI = f'sqlite:///{database_path}'
# SQLAlchemyの設定
SQLALCHEMY_TRACK_MODIFICATIONS = False
# Azure Blob Storage のデータベースファイル用の SAS URL
# BLOB_DB_URL = os.environ.get("BLOB_DB_URL", "https://btudio.blob.core.windows.net/bisdom/database.db?sp=r&st=2025-03-19T15:22:04Z&se=2025-03-19T23:22:04Z&skoid=a9061414-2f57-4899-b404-91e85fe0d848&sktid=7e4dddc4-eabb-4e24-8a00-3347e5541552&skt=2025-03-19T15:22:04Z&ske=2025-03-19T23:22:04Z&sks=b&skv=2022-11-02&sv=2022-11-02&sr=b&sig=tdVRRiv5eAb7pMujP%2Fr9j3HQTRPoIFp7Kx3Hm2xrqf8%3D")
BLOB_DB_URL = "https://btudio.blob.core.windows.net/bisdom/database.db?sp=rw&st=2025-03-19T15:22:04Z&se=2025-03-25T23:22:04Z&skoid=a9061414-2f57-4899-b404-91e85fe0d848&sktid=7e4dddc4-eabb-4e24-8a00-3347e5541552&skt=2025-03-19T15:22:04Z&ske=2025-03-25T23:22:04Z&sks=b&skv=2022-11-02&sv=2022-11-02&sr=b&sig=SS2VQPq3Trd1P3IcFWW3xYHmOUxbknEvSSrKJS0rsXQ%3D"

class TestingConfig:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'bisdom20252HBXXXWGFIRSTTRIAL'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=1)
    JWT_COOKIE_HTTPONLY = True
    JWT_TOKEN_LOCATION = ['headers', 'cookies']
    JWT_COOKIE_SECURE = True
    JWT_REFRESH_COOKIE_PATH ="/refresh"
