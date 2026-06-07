from fastapi import APIRouter, status
from app.schemas.leave_schema import LeaveRequestCreate
from app.services.leave_service import LeaveService

router = APIRouter(prefix="/api/v1/leaves", tags=["Leaves System"])

@router.post("/request", status_code=status.HTTP_201_CREATED, summary="พนักงานยื่นคำขอลาใหม่")
def request_leave(payload: LeaveRequestCreate):
    # เรียกใช้คำสั่งตรวจสอบเงื่อนไขจาก Service
    validation_result = LeaveService.validate_and_calculate_leave(payload)
    
    # ฐานข้อมูลเสมือนจำลองว่าเซฟสำเร็จ (Mock Database Insert)
    return {
        "success": True,
        "message": "ส่งคำขอลาสำเร็จแล้ว ระบบกำลังรอการอนุมัติจากหัวหน้างาน",
        "metadata": {
            "emp_id": payload.emp_id,
            "leave_type": payload.leave_type,
            "calculated_days": validation_result["total_days"],
            "current_status": validation_result["status"]
        }
    }