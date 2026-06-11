from fastapi import FastAPI
from app.routes.usuarios import router as usuarios_router
from app.database import db

app = FastAPI(
    title="DataPulse API",
    version="1.0.0"
)

app.include_router(usuarios_router)

@app.get("/")
def inicio():
    return {"mensaje": "Backend de DataPulse funcionando"}

@app.get("/test-db")
def test_db():
    db.command("ping")
    return {"mensaje": "MongoDB conectado correctamente"}