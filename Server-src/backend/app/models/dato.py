from sqlalchemy import Column, Integer, Float, String

from app.database.database import Base


class DatosCETEVI(Base):
    __tablename__ = "DatosCETEVI"

    id = Column(Integer, autoincrement=True, primary_key=True)

    Id = Column(
        String
    )

    Caso = Column(String)

    Tiempo = Column(Float)

    Fuerza = Column(Float)

    Corriente = Column(Float)

