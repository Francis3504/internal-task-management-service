from sqlalchemy.orm import relationship
from sqlalchemy import Column,INTEGER,String,DATETIME,BOOLEAN,ForeignKey
from datetime import datetime
from database.db import Base

class Task(Base):
    __tablename__="tasks"
    id=Column(INTEGER,primary_key=True)
    title=Column(String,nullable=False)
    description=Column(String,nullable=False)
    created_at=Column(DATETIME,nullable=True)
    deadline=Column(DATETIME,nullable=False)
    is_completed=Column(BOOLEAN,nullable=False)
    department_id=Column(INTEGER,ForeignKey("departments.id"),nullable=False)
    created_by_id=Column(INTEGER,ForeignKey("users.id"),nullable=True)
    department=relationship("Department",back_populates="tasks")
    assignments=relationship("TaskAssignment",back_populates="task")


class TaskAssignment(Base):
    __tablename__="task_assignments"

    id=Column(INTEGER,primary_key=True)
    task_id=Column(INTEGER,ForeignKey("tasks.id"),nullable=False)
    user_id=Column(INTEGER,ForeignKey("users.id"),nullable=False)

    task=relationship("Task",back_populates="assigments")
    user=relationship("User",back_populates="tasks")