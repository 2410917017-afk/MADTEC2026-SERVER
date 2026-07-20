from sqlalchemy import Column, Integer, String, Float
from app.database.database import Base


class CasoSoldadura(Base):

    __tablename__= "CasosSoldadura"

    id = Column(Integer, primary_key=True, index=True)

    Nombre = Column(String(300), nullable=False)

    Tiempo = Column(Float)

    Fuerza = Column(Float)

    Compresion = Column(Float)

    Pulsos = Column(Integer)

    Material = Column(String(300))

    Grosor = Column(Float)

    Separacion = Column(Float)
