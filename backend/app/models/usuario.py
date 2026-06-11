from pydantic import BaseModel, EmailStr

class Usuario(BaseModel):
    cedula: str
    nombre: str
    correo: EmailStr
    password: str
    rol: str
    estado: bool = True