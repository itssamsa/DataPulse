from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.database import db
from app.services.excel_service import generar_excel
from app.services.pdf_service import generar_pdf

router = APIRouter()

@router.get("/reportes/usuarios/{empresa_id}")
def reporte_usuarios(
    empresa_id: str,
    formato: str = "excel"
):

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

    if formato == "excel":

        archivo = generar_excel(
            usuarios,
            empresa_id
        )

        return FileResponse(
            archivo,
            filename=archivo
        )

    if formato == "pdf":

        archivo = generar_pdf(
            usuarios,
            empresa_id
        )

        return FileResponse(
            archivo,
            filename=archivo
        )

    return {
        "mensaje": "Formato no válido"
    }