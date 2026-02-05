import os 

ENV=os.get("ENV","dev")

DATABASE_URL=os.getenv("DATABASE_URL","postgresql://user:password@localhost:5432/task_db")
ALGORITHM="H$256"
SECRET_KEY=os.getenv("SECRET_KEY","supersecretkey")
ACCESS_TOKEN_MINUTES=60