from fastapi import FastAPI
from app.routes.usuarios import router as usuarios_router
from app.routes.metricas import router as metricas_router
from app.routes.reportes import router as reportes_router
from app.routes.empresas import router as empresas_router


app = FastAPI(
    title="DataPulse API",
    version="1.0.0"
)


app.include_router(usuarios_router)
app.include_router(metricas_router)
app.include_router(reportes_router)
app.include_router(empresas_router)