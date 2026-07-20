from pydantic import BaseModel


class CasoBase(BaseModel):
    Nombre: str
    Tiempo: float
    Fuerza: float
    Compresion: float
    Pulsos: int
    Material: str
    Grosor: float
    Separacion: float



class CasoCreate(CasoBase):
    pass

class CasoUpdate(CasoBase):
    pass


class CasoResponse(CasoBase):
    id: int

    class Config:
        from_attributes = True
