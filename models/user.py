from sqlalchemy import Column,Integer,String,ForeignKey,Enum
from sqlalchemy.orm import relationship
from database.db import Base
from enum import Enum as enumm

class UserStaus(enumm):
    MEMBER="member"
    LEADER="leader"


class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    first_name=Column(String,nullable=True)
    middle_name=Column(String,nullable=True)
    last_name=Column(String,nullable=False)
    email=Column(String,unique=True,index=True,nullable=True)
    password_hash=Column(String,nullable=False)
    role=Column(Enum(UserStaus),nullable=False)
    department_id=Column(Integer,ForeignKey("departments.id"),nullable=True)
    department=relationship("Department",back_populates="users")
    tasks=relationship("TaskAssignment",back_populates="user")