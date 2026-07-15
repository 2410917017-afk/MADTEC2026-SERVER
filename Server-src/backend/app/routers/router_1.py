from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.dato import DatosCETEVI
from app.schemas.datos import DatosCreate, DatosResponse

router = APIRouter(
    prefix="/datos",
    tags=["Datos"]
)


@router.post("/", response_model=DatosResponse)
def crear_dato(dato: DatosCreate, db: Session = Depends(get_db)):

    nuevo = DatosCETEVI(

        Id=dato.Id,
        Caso=dato.Caso,
        Tiempo=dato.Tiempo,
        Fuerza=dato.Fuerza,
        Corriente=dato.Corriente
    )

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return nuevo


@router.get("/", response_model=list[DatosResponse])
def obtener_datos(db: Session = Depends(get_db)):
    return db.query(DatosCETEVI).all()
