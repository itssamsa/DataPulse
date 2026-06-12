from fastapi import APIRouter
from app.models.login import Login
from app.database import db
from app.models.usuario import Usuario

router = APIRouter()

# crud 
#crear usuario
@router.post("/usuarios")
def crear_usuario(usuario: Usuario):

    existe = db.usuarios.find_one(
        {"cedula": usuario.cedula}
    )

    if existe:
        return {
            "mensaje": "Ya existe un usuario con esta cédula"
        }

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

# Listar usuarios 
@router.get("/usuarios")
def listar_usuarios():

    usuarios = list(
        db.usuarios.find(
            {},
            {"_id": 0}
        )
    )

    return usuarios

# Obtener usuario por cédula
@router.get("/usuarios/{cedula}")
def obtener_usuario(cedula: str):

    usuario = db.usuarios.find_one(
        {"cedula": cedula},
        {"_id": 0}
    )

    if usuario:
        return usuario

    return {"mensaje": "Usuario no encontrado"}

# actualizar usuario
@router.put("/usuarios/{cedula}")
def actualizar_usuario(cedula: str, usuario: Usuario):

    resultado = db.usuarios.update_one(
        {"cedula": cedula},
        {
            "$set": {
                "nombre": usuario.nombre,
                "correo": usuario.correo,
                "password": usuario.password,
                "rol": usuario.rol,
                "estado": usuario.estado
            }
        }
    )

    if resultado.modified_count > 0:
        return {"mensaje": "Usuario actualizado correctamente"}

    return {"mensaje": "Usuario no encontrado o sin cambios"}

# eliminar usuario
@router.delete("/usuarios/{cedula}")
def eliminar_usuario(cedula: str):

    resultado = db.usuarios.update_one(
        {"cedula": cedula},
        {
            "$set": {
                "estado": False
            }
        }
    )

    if resultado.modified_count > 0:
        return {"mensaje": "Usuario desactivado correctamente"}

    return {"mensaje": "Usuario no encontrado"}

#Se creó el modelo de usuario y se desarrollaron las funciones para registrar, consultar, actualizar y gestionar usuarios dentro del sistema.
# para la eliminación se decidió no borrar completamente los datos del usuario sino que mejor se cambia el estado a False para mantener el historial y conservar la información en caso de que sea necesaria más adelante.
# ----la primera versión del CRUD de usuarios-----

#Login - inicio de sesión

@router.post("/login")
def iniciar_sesion(datos: Login):

    usuario = db.usuarios.find_one(
        {
            "correo": datos.correo,
            "password": datos.password,
            "estado": True
        },
        {"_id": 0}
    )

    if usuario:
        return {
            "mensaje": "Inicio de sesión exitoso",
            "usuario": usuario
        }

    return {
        "mensaje": "Correo o contraseña incorrectos"
    }

#Perfil de usuario - obtener información del perfil por cédula
@router.get("/perfil/{cedula}")
def obtener_perfil(cedula: str):

    usuario = db.usuarios.find_one(
        {"cedula": cedula},
        {
            "_id": 0,
            "password": 0
        }
    )

    if usuario:
        return usuario

    return {
        "mensaje": "Usuario no encontrado"
    }