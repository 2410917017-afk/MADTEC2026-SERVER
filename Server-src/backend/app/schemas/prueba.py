from pydantic import BaseModel


class PruebaBase(BaseModel):
    Id: str
    Caso: str
    Muestras: int
    Tiempo: float
    FMax: float
    IMax: float
    Diametro: float


class PruebaCreate(PruebaBase):
    pass


class PruebaResponse(PruebaBase):
    class Config:
        from_attributes = True
