from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional, Annotated


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    
    
class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: str
    created_at: datetime

class PostsReponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    
class PostOut(BaseModel):
    Post: PostsReponse
    votes: int
    
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token : str
    token_type : str
    
class TokenData(BaseModel):
    id : Optional[str] = None
    
class Vote(BaseModel):
    post_id: int
    direction: Annotated[int,conint(le=1)]
