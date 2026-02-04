from pydantic import BaseModel

class DepartmentOut(BaseModel):
    id:int
    name:str

    class Config:
        orm_mode=True