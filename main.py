from fastapi import FastAPI, Path ,status
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import BaseModel
from scraper import scrape
from email_sender import emailsender
app = FastAPI()

class Student(BaseModel):
    subject: str = None
    to: str = None
    body: str=None

@app.get("/")
def index():
    return {"message": "Welcome to a classroom example of FastAPI!"}

@app.get("/getemails/{query}")
async def search_email(query: str,pages: int =2):
    result=await scrape(query, pages)
    return {"emails": result}

@app.post("/sendemail")
def send(student: Student):
    emailsender(student.to,student.subject,student.body)
    return JSONResponse(status_code=status.HTTP_200_OK)
