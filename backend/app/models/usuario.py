from pydantic import BaseModel, EmailStr
from typing import Literal


class Usuario(BaseModel):

    cedula: str
    nombre: str
    correo: EmailStr
    password: str
    rol: Literal[
        "Administrador",
        "Analista",
        "Usuario general"
    ]
    empresa_id: str
    estado: bool = True 