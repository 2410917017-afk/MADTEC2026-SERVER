from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.caso import CasoSoldadura

from app.schemas.casos import CasoCreate, CasoResponse, CasoUpdate

router = APIRouter(
    prefix="/casos",
    tags=["Casos de soldadura"]
)

@router.post("/", response_model=CasoResponse)
def crear_caso(caso: CasoCreate, db: Session = Depends(get_db)):

    nuevo = CasoSoldadura(
        Nombre=caso.Nombre,
        Tiempo=caso.Tiempo,
        Fuerza=caso.Fuerza,
        Compresion=caso.Compresion,
        Pulsos=caso.Pulsos,
        Material=caso.Material,
        Grosor=caso.Grosor,
        Separacion=caso.Separacion,
        Proximidad=caso.Proximidad,

    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return nuevo

@router.put("/{id}", response_model=CasoResponse)
def actualizar_caso(
    id: int,
    datos: CasoUpdate,
    db: Session = Depends(get_db)
):

    caso = db.query(CasoSoldadura).filter(
        CasoSoldadura.id == id
    ).first()

    if caso is None:
        raise HTTPException(
            status_code=404,
            detail="Caso no encontrado"
        )

    caso.Nombre = datos.Nombre
    caso.Tiempo = datos.Tiempo
    caso.Fuerza = datos.Fuerza
    caso.Compresion = datos.Compresion
    caso.Pulsos = datos.Pulsos
    caso.Material = datos.Material
    caso.Grosor = datos.Grosor
    caso.Separacion = datos.Separacion
    caso.Proximidad = datos.Proximidad

    db.commit()
    db.refresh(caso)

    return caso

@router.delete("/{id_caso}")
def eliminar_caso(id_caso: int, db: Session = Depends(get_db)):

    caso = db.query(CasoSoldadura).filter(
        CasoSoldadura.id == id_caso
    ).first()

    if caso is None:
        raise HTTPException(
            status_code=404,
            detail="Caso no encontrado"
        )

    db.delete(caso)
    db.commit()

    return {"mensaje": "Caso eliminado correctamente"}

@router.get("/", response_model=list[CasoResponse])
def obtener_casos(db: Session = Depends(get_db)):
    return db.query(CasoSoldadura).all()


@router.get("/{id}", response_model=CasoResponse)
def obtener_caso(id: int, db: Session = Depends(get_db)):

    caso = db.query(CasoSoldadura).filter(
        CasoSoldadura.id == id
    ).first()

    if caso is None:
        raise HTTPException(
            status_code=404,
            detail="Caso no encontrado"
        )

    return caso
