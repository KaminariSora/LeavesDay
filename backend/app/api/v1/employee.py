from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.employee_schema import CreateUser
from app.models.employee import EmployeeModel

router = APIRouter(prefix="/api/v1/employees", tags=["Employees"])

@router.post("/register", status_code=status.HTTP_201_CREATED, summary="สร้างรายชื่อพนักงานใหม่ใน DB")
def register_employee(payload: CreateUser, db: Session = Depends(get_db)):
    existing_user = db.query(EmployeeModel).filter(EmployeeModel.email == payload.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="อีเมลนี้ถูกลงทะเบียนในระบบเรียบร้อยแล้ว"
        )
    
    new_employee = EmployeeModel(
        name=payload.name,
        lastname=payload.lastname,
        email=payload.email,
        position=payload.position,
        department=payload.department,
        section=payload.section,
        division=payload.division
    )
    
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return {
        "success": True,
        "message": "เพิ่มข้อมูลพนักงานใหม่เรียบร้อยแล้ว",
        "data": {
            "id": str(new_employee.id),
            "email": new_employee.email
        }
    }