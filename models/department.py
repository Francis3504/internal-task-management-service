from sqlalchemy.orm import relationship
from database.db import Base
from sqlalchemy import Column,String,INTEGER


class DepartMent(Base):
    __tablename__="departments"

    id=Column(INTEGER,primary_key=True)
    name=Column(String,nullable=False)

    users=relationship("User",back_populates="department")
    tasks=relationship("Task",back_populates="department")