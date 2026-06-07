from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings

# 1. สร้าง Engine ตัวขับเคลื่อนการเชื่อมต่อ (สำหรับ NeonDB ต้องเปิด sslmode=require เสมอ)
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True  # คอยเช็กว่าแนวเชื่อมต่อหลุดหรือไม่ (จำเป็นมากสำหรับ Serverless DB)
)

# 2. สร้าง Session Local สำหรับให้ API แต่ละเส้นหยิบไปใช้ยิง Query
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Base class สำหรับให้ไฟล์ในโฟลเดอร์ models/ อื่นๆ นำไปสืบทอดเพื่อแปลงร่างเป็นตาราง DB
Base = declarative_base()

# Dependency สำหรับใช้ใน FastAPI Endpoints (คอยสร้างและปิด Session อัตโนมัติเมื่อทำงานเสร็จ)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()