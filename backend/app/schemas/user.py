from pydantic import BaseModel, EmailStr

class UserCreatE(BaseModel):
    email: EmailStr
    password: str
    

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    

class UserOut(BaseModel):
    id: int
    email: EmailStr
    
    class config:
        orm_mode = True