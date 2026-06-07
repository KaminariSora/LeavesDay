from pydantic import BaseModel, Field
from datetime import date
from typing import Optional
from enum import Enum

# Enum กำหนดรูปแบบการลา
class LeaveFormat(str, Enum):
    FULL = "Full"            # เต็มวัน
    MORNING = "Morning"      # ครึ่งวันเช้า
    AFTERNOON = "Afternoon"  # ครึ่งวันบ่าย

# Enum ประเภทการลา
class LeaveTypeEnum(str, Enum):
    SICK = "Sick"            # ลาป่วย
    PERSONAL = "Personal"    # ลากิจ
    VACATION = "Vacation"    # ลาพักร้อน

class LeaveRequestCreate(BaseModel):
    emp_id: str = Field(..., example="EMP001", description="รหัสพนักงาน")
    leave_type: LeaveTypeEnum = Field(..., example=LeaveTypeEnum.VACATION)
    start_date: date = Field(..., example="2026-06-15")
    end_date: date = Field(..., example="2026-06-17")
    leave_format: LeaveFormat = Field(..., example=LeaveFormat.FULL)
    reason: str = Field(..., example="ติดธุระสำคัญที่ต่างจังหวัด")
    medical_cert_url: Optional[str] = Field(None, example="https://storage.com/cert.jpg")