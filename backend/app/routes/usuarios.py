from fastapi import APIRouter
from app.models.login import Login
from app.database import db
from app.models.usuario import Usuario

router = APIRouter()

# Crear usuario
@router.post("/usuarios")
def crear_usuario(usuario: Usuario):

    existe = db.usuarios.find_one(
        {
            "$or": [
                {
                    "cedula": usuario.cedula,
                    "empresa_id": usuario.empresa_id
                },
                {
                    "correo": usuario.correo,
                    "empresa_id": usuario.empresa_id
                }
            ]
        }
    )

    if existe:
        return {
            "mensaje": "La cédula o el correo ya están registrados en esta empresa"
        }

    nuevo_usuario = {
        "cedula": usuario.cedula,
        "nombre": usuario.nombre,
        "correo": usuario.correo,
        "password": usuario.password,
        "rol": usuario.rol,
        "empresa_id": usuario.empresa_id,
        "estado": usuario.estado
    }

    resultado = db.usuarios.insert_one(nuevo_usuario)

    return {
        "mensaje": "Usuario creado correctamente",
        "id": str(resultado.inserted_id)
    }


# Obtener usuario por cédula dentro de una empresa
@router.get("/usuarios/{empresa_id}/{cedula}")
def obtener_usuario(empresa_id: str, cedula: str):

    usuario = db.usuarios.find_one(
        {
            "cedula": cedula,
            "empresa_id": empresa_id
        },
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

# Listar usuarios de una empresa
@router.get("/usuarios/empresa/{empresa_id}")
def listar_usuarios_empresa(empresa_id: str):

    usuarios = list(
        db.usuarios.find(
            {
                "empresa_id": empresa_id
            },
            {
                "_id": 0,
                "password": 0
            }
        )
    )

    return usuarios

# Actualizar usuario
@router.put("/usuarios/{empresa_id}/{cedula}")
def actualizar_usuario(
    empresa_id: str,
    cedula: str,
    usuario: Usuario
):

    resultado = db.usuarios.update_one(
        {
            "cedula": cedula,
            "empresa_id": empresa_id
        },
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
        return {
            "mensaje": "Usuario actualizado correctamente"
        }

    return {
        "mensaje": "Usuario no encontrado o sin cambios"
    }

# Desactivar usuario (no lo borra, solo cambia su estado a inactivo - esto para mantener el historial de datos relacionados con ese usuario-)
@router.delete("/usuarios/{empresa_id}/{cedula}")
def eliminar_usuario(
    empresa_id: str,
    cedula: str
):

    resultado = db.usuarios.update_one(
        {
            "cedula": cedula,
            "empresa_id": empresa_id
        },
        {
            "$set": {
                "estado": False
            }
        }
    )

    if resultado.modified_count > 0:
        return {
            "mensaje": "Usuario desactivado correctamente"
        }

    return {
        "mensaje": "Usuario no encontrado"
    }

# Login
@router.post("/login")
def iniciar_sesion(datos: Login):

    usuario = db.usuarios.find_one(
        {
            "correo": datos.correo,
            "password": datos.password,
            "estado": True
        },
        {
            "_id": 0,
            "password": 0
        }
    )

    if usuario:

        return {
            "mensaje": "Inicio de sesión exitoso",
            "usuario": usuario
        }

    return {
        "mensaje": "Correo o contraseña incorrectos"
    }

# Perfil
@router.get("/perfil/{empresa_id}/{cedula}")
def obtener_perfil(
    empresa_id: str,
    cedula: str
):

    usuario = db.usuarios.find_one(
        {
            "cedula": cedula,
            "empresa_id": empresa_id
        },
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