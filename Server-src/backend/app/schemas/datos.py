from pydantic import BaseModel


class DatosBase(BaseModel):

    Id: str
    Caso: str
    Tiempo: float
    Fuerza: float
    Corriente: float


class DatosCreate(DatosBase):
    pass


class DatosResponse(DatosBase):
    class Config:
        from_attributes = True
