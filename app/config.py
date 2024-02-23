import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.getcwd(), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    def __init__(self):
        self.DB_NAME = os.getenv("DB_NAME")
        self.DB_USER = os.getenv("DB_USER")
        self.DB_PASSWORD = os.getenv("DB_PASSWORD")
        self.DB_HOST = os.getenv("DB_HOST")
        self.DB_PORT = os.getenv("DB_PORT")
        self.DB_URL = os.getenv("DB_URL")

    def __str__(self):
        return f"{self.DB_URL}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

