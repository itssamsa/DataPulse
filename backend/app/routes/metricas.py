from fastapi import APIRouter
from app.database import db

router = APIRouter()

@router.get("/metricas/{empresa_id}")
def obtener_metricas(empresa_id: str):

    total = db.usuarios.count_documents(
        {
            "empresa_id": empresa_id
        }
    )

    activos = db.usuarios.count_documents(
        {
            "empresa_id": empresa_id,
            "estado": True
        }
    )

    inactivos = db.usuarios.count_documents(
        {
            "empresa_id": empresa_id,
            "estado": False
        }
    )

    administradores = db.usuarios.count_documents(
        {
            "empresa_id": empresa_id,
            "rol": "Administrador"
        }
    )

    analistas = db.usuarios.count_documents(
        {
            "empresa_id": empresa_id,
            "rol": "Analista"
        }
    )

    usuarios_generales = db.usuarios.count_documents(
        {
            "empresa_id": empresa_id,
            "rol": "Usuario general"
        }
    )

    return {
        "empresa_id": empresa_id,
        "total_usuarios": total,
        "usuarios_activos": activos,
        "usuarios_inactivos": inactivos,
        "administradores": administradores,
        "analistas": analistas,
        "usuarios_generales": usuarios_generales
    }