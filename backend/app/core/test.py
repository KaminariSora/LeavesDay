import os
from dotenv import load_dotenv

# โหลดค่าจากไฟล์ .env
load_dotenv()
print(os.getenv("NEONDB_URL"))