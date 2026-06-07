from pydantic import BaseModel, Field
import uuid

class CreateUser(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, description="รหัสพนักงานในรูปแบบ UUID")
    name: str = Field(..., example="Somchai")
    lastname: str = Field(..., example="Deejai")
    email: str = Field(..., example="somchai@company.com")
    position: str = Field(..., example="NormalSalaryMan")
    department: str = Field(..., example="Department")
    section: str = Field(..., example="Section")
    division: str = Field(..., example="Division")

