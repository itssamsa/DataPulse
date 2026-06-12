from pydantic import BaseModel, EmailStr

class Login(BaseModel):
    correo: EmailStr
    password: str