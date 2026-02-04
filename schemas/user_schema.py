from pydantic import BaseModel,Field,EmailStr
from typing import Optional
from enum import Enum

class UserRole(str,Enum):
    MEMBER="member"
    LEADER="leader"

class UserCreate(BaseModel):
    first_name:str=Field(min_length=3)
    middle_name:Optional[str]=None
    last_name:str=Field(min_length=3)
    email:EmailStr
    password:str=Field(min_length=8)
    role:UserRole
    department_id:int


class UserLogin(BaseModel):
    emial:EmailStr
    password:str=Field(min_length=8)

class UserOut(BaseModel):
    id:int
    first_name:str
    middle_name:Optional[str]
    last_name:str
    email:EmailStr
    role:UserRole
    department_id:int

    class Config:
        orm_mode=True