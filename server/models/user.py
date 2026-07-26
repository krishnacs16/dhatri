from pydantic import BaseModel
from enum import Enum
from typing import Optional

class UserType(str, Enum):
    DOCTOR = "doctor"
    PATIENT = "patient"
    ADMIN = "admin"
    STAFF = "staff"
    

class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
    type: UserType
    last_login: datetime | None = None

