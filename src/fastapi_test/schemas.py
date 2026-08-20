from pydantic import BaseModel
##Base Model is used for data validation and parsing 
class PostCreate (BaseModel):
    title: str
    content: str