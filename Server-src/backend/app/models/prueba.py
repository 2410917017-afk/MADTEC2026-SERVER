from sqlalchemy import Column, Integer, String, Float

from app.database.database import Base


class PruebasCETEVI(Base):
    __tablename__ = "PruebasCETEVI"

    Id = Column(String(300), primary_key=True)

    Caso = Column(String)

    Muestras = Column(Integer)

    Tiempo = Column(Float)

    FMax = Column(Float)

    IMax = Column(Float)

    Diametro = Column(Float)

