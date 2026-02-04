from pydantic import BaseModel,Field

class UserCreate(BaseModel):
    first_name:str=Field(min_length=3)
    middle_name:str
    last_name:str=Field(min_length=3)
    email:str
    password:str=Field(min_length=8)
    postion:str
    department:str


class UserLogin(BaseModel):
    emial:str
    password:str=Field(min_length=8)