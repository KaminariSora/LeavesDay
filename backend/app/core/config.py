import os
from dotenv import load_dotenv

# โหลดค่าจากไฟล์ .env
load_dotenv()

class Settings:
    PROJECT_NAME: str = "LeavesDay API"
    DATABASE_URL: str = os.getenv("NEONDB_URL")

settings = Settings()