from pydantic import BaseModel,EmailStr,conint
from datetime import datetime
from typing import Optional


class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime

    class Config:
        orm_mode=True

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase): #here we inheritate the PostBase class
    pass


class Post(PostBase):
    id:int
    created_at:datetime
    owner_id: int
    owner:UserOut

    class Config:
        orm_mode=True

class UserCreate(BaseModel):
    email:EmailStr
    password:str


    
class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:Optional[str]=None
    

class Vote(BaseModel):
    post_id:int
    dir:conint(le=1) #what this does is let user only do 2 thing vote or remove vote 1 means vote 0 mean unvote

class PostOut(BaseModel):
    Post:Post
    votes:int

    class Config:
        orm_mode=True