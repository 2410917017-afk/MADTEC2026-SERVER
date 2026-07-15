from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.prueba import PruebasCETEVI
from app.schemas.prueba import PruebaCreate, PruebaResponse

router = APIRouter(
    prefix="/pruebas",
    tags=["Pruebas"]
)

@router.post("/", response_model=PruebaResponse)
def crear_prueba(prueba: PruebaCreate, db: Session = Depends(get_db)):

    nueva = PruebasCETEVI(

        Id=prueba.Id,
        Caso=prueba.Caso,
        Muestras=prueba.Muestras,
        Tiempo=prueba.Tiempo,
        FMax=prueba.FMax,
        IMax=prueba.IMax,
        Diametro=prueba.Diametro
    )

    db.add(nueva)
    db.commit()
    db.refresh(nueva)

    return nueva


@router.get("/", response_model=list[PruebaResponse])
def obtener_pruebas(db: Session = Depends(get_db)):
    return db.query(PruebasCETEVI).all()
