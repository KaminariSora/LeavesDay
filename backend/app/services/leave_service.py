from datetime import date, datetime
from fastapi import HTTPException, status
from app.schemas.leave_schema import LeaveRequestCreate, LeaveTypeEnum

class LeaveService:
    @staticmethod
    def validate_and_calculate_leave(payload: LeaveRequestCreate):
        today = date.today()
        
        # 1. เช็กความถูกต้องของวันที่ขั้นแรก
        if payload.start_date > payload.end_date:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="วันที่เริ่มลาต้องไม่เกินวันที่สิ้นสุดการลา"
            )

        # คำนวณจำนวนวันลาเบื้องต้น (รวมวันเริ่มและวันจบ)
        # ในระบบจริง ส่วนนี้จะต้องดึงตารางวันหยุดบริษัทมาหักเสาร์-อาทิตย์ออกด้วย
        total_days = (payload.end_date - payload.start_date).days + 1
        
        # หากลาครึ่งวัน ให้ปรับจำนวนวันเหลือ 0.5 วันทันที
        if payload.leave_format in ["Morning", "Afternoon"]:
            total_days = 0.5

        # 2. ตรวจสอบกฎการลากล่วงหน้า (min_lead_days)
        days_in_advance = (payload.start_date - today).days

        if payload.leave_type == LeaveTypeEnum.VACATION and days_in_advance < 3:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="ลาพักร้อนต้องแจ้งล่วงหน้าอย่างน้อย 3 วัน"
            )
            
        if payload.leave_type == LeaveTypeEnum.PERSONAL and days_in_advance < 1:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="ลากิจต้องแจ้งล่วงหน้าอย่างน้อย 1 วัน"
            )

        # 3. ตรวจสอบเงื่อนไขใบรับรองแพทย์สำหรับการลาป่วยตั้งแต่ 3 วันขึ้นไป
        if payload.leave_type == LeaveTypeEnum.SICK and total_days >= 3:
            if not payload.medical_cert_url:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="ลาป่วยตั้งแต่ 3 วันขึ้นไป จำเป็นต้องแนบใบรับรองแพทย์"
                )

        # ผ่านทุกเงื่อนไข ส่งข้อมูลพร้อมบันทึก (ในงานจริงจะคืนค่าเพื่อส่งต่อไปยัง Repository เพื่อ Insert ลง DB)
        return {
            "total_days": total_days,
            "status": "Pending"
        }