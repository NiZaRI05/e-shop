import os
from dotenv import load_dotenv 1

load_dotenv()

class Config:
    SECRET_KEY = OS.GETENV('SECRET_KEY','dev-secret')
    # COnfiguracion de la BD
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://(os.getenv('DB_USER')):(os.getenv('DB_PASSWORD'))"
        f"@(os.getenv('DB_HOST'))/(os.getenv('DB_NAME'))"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False