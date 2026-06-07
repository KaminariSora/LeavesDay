from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.leaves import router as leaves_router
from app.api.v1.employee import router as employee_router

app = FastAPI(
    title="LeavesDay Backend API",
    description="ระบบบริหารจัดการวันลาและเวลาเข้างานของพนักงาน",
    version="1.0.0"
)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. นำ Router ของระบบลาเข้ามาผูกกับระบบใหญ่
# หลังบ้านจะทำการเอา prefix "/api/v1/leaves" ไปต่อให้โดยอัตโนมัติ
app.include_router(leaves_router)
app.include_router(employee_router)

@app.get("/", summary="Welcome Page", tags=["General"])
def read_root():
    return {
        "status": "online",
        "message": "Leave days API",
        "documentation": "http://127.0.0.1:8000/docs"
    }