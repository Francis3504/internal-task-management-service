import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app=FastAPI(title=os.getenv("APP_NAME"))

@app.get("/hello")
def greeting():
    return {"message":"Hello there"}