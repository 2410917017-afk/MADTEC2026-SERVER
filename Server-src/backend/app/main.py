from fastapi import FastAPI
from app.database.database import engine
from app.database.database import Base
from contextlib import asynccontextmanager
from app.routers import router_1
from app.routers import pruebas
from app.routers import casos

import app.models


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Servidor cetevi_1",
    version="0.1.0",
    description="API para adquisición de datos de laboratorio CETEVI-UAQ"
)

app.include_router(router_1.router)
app.include_router(pruebas.router)
app.include_router(casos.router)

@app.get("/")
async def root():
    return {
        "status": "ok",
        "message": "Servidor funcionando"
    }


