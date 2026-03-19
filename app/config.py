import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ENV = os.getenv("ENV", "dev")
    if ENV not in ["dev", "staging", "prod"]:
        raise ValueError("ENV must be 'dev', 'staging', or 'prod'")

    DATABASES = {
        "dev": os.getenv("DATABASE_URL_DEV"),
        "staging": os.getenv("DATABASE_URL_STAGING"),
        "prod": os.getenv("DATABASE_URL_PROD")
    }

    SQLALCHEMY_DATABASE_URI = DATABASES.get(ENV)
    if SQLALCHEMY_DATABASE_URI is None:
        raise ValueError(f"No database configured for environment: {ENV}")

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # ⚡ Recommandé pour éviter les warnings

    @classmethod
    def debug(cls):
        print(f"[CONFIG] ENV={cls.ENV}, DATABASE_URL={cls.SQLALCHEMY_DATABASE_URI[:50]}...")


