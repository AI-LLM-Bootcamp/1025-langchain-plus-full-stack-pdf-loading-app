from pydantic import BaseModel
from typing import Optional

class PDFRequest(BaseModel):
    name: str
    selected: bool
    file: str

class PDFResponse(BaseModel):
    id: int
    name: str
    selected: bool
    file: str

    class Config:
        from_attributes = True

#For PDF QA    
class QuestionRequest(BaseModel):
    question: str
