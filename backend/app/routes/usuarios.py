from fastapi import APIRouter
from app.database import db
from app.models.usuario import Usuario

router = APIRouter()

@router.post("/usuarios")
def crear_usuario(usuario: Usuario):

    nuevo_usuario = {
        "cedula": usuario.cedula,
        "nombre": usuario.nombre,
        "correo": usuario.correo,
        "password": usuario.password,
        "rol": usuario.rol,
        "estado": usuario.estado
    }

    resultado = db.usuarios.insert_one(nuevo_usuario)

    return {
        "mensaje": "Usuario creado correctamente",
        "id": str(resultado.inserted_id)
    }