import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL=os.getenv("DATABASE_URL","postgresql://user:pass@localhost/task_manager_db")
engine=create_engine(DATABASE_URL,echo=True,pool_pre_ping=True)

Session=sessionmaker(expire_on_commit=False,autoflush=False,bind=engine)

Base=declarative_base()