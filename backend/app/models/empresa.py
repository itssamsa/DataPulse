from pydantic import BaseModel

class Empresa(BaseModel):
    nombre: str
    nit: str
    estado: bool = True