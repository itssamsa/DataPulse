from fastapi import APIRouter
from app.database import db
from app.models.empresa import Empresa

router = APIRouter()

# Crear empresa
@router.post("/empresas")
def crear_empresa(empresa: Empresa):

    existe = db.empresas.find_one(
        {
            "nit": empresa.nit
        }
    )

    if existe:
        return {
            "mensaje": "Ya existe una empresa con este NIT"
        }

    nueva_empresa = {
        "nombre": empresa.nombre,
        "nit": empresa.nit,
        "estado": empresa.estado
    }

    resultado = db.empresas.insert_one(
        nueva_empresa
    )

    return {
        "mensaje": "Empresa creada correctamente",
        "id": str(resultado.inserted_id)
    }

# Listar empresas
@router.get("/empresas")
def listar_empresas():

    empresas = list(
        db.empresas.find(
            {},
            {
                "_id": 0
            }
        )
    )


    return empresas

# Obtener empresa por NIT
@router.get("/empresas/{nit}")
def obtener_empresa(nit: str):

    empresa = db.empresas.find_one(
        {
            "nit": nit
        },
        {
            "_id": 0
        }
    )

    if empresa:
        return empresa

    return {
        "mensaje": "Empresa no encontrada"
    }

# Desactivar empresa
@router.delete("/empresas/{nit}")
def eliminar_empresa(nit: str):

    resultado = db.empresas.update_one(
        {
            "nit": nit
        },
        {
            "$set": {
                "estado": False
            }
        }
    )

    if resultado.modified_count > 0:
        return {
            "mensaje": "Empresa desactivada"
        }

    return {
        "mensaje": "Empresa no encontrada"
    }