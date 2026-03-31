import os

class Config:
    ENV = os.getenv("ENV")

    if not ENV:
        raise ValueError("ENV is not set")

    DATABASE_URL = os.getenv("DATABASE_URL")

    if not DATABASE_URL:
        raise ValueError("DATABASE_URL is not set")

    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @classmethod
    def debug(cls):
        print(f"[CONFIG] ENV={cls.ENV}, DB={cls.SQLALCHEMY_DATABASE_URI[:50]}...")