from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base
import uuid

class EmployeeModel(Base):
    __tablename__ = "users"  # ต้องชื่อตรงกับตารางใน NeonDB

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    position = Column(String(100))
    department = Column(String(100))
    section = Column(String(100))
    division = Column(String(100))