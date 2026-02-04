from pydantic import BaseModel
from typing import Optional,List

class TaskCreate(BaseModel):
    title:str
    description:str
    deadline:str
    assignee_id:List[int]=[]


class TaskOut(BaseModel):
    id:int
    title:str
    descrption:str
    created_at:str
    deadline:str
    is_completed:bool
    department_id:int
    created_by_id:int
    assignee_ids:List[int]=[]

    class Confg:
        orm_mode=True