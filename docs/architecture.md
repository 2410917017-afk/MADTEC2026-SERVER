# Arquitectura

El servidor esta organizado como una API FastAPI con persistencia en PostgreSQL mediante SQLAlchemy.

## Componentes

- `app/main.py`: crea la aplicacion FastAPI, registra routers y crea tablas con `Base.metadata.create_all`.
- `app/database/database.py`: configura `DATABASE_URL`, el `engine`, `SessionLocal` y la dependencia `get_db`.
- `app/models`: define las tablas SQLAlchemy.
- `app/schemas`: define los contratos Pydantic usados en requests y responses.
- `app/routers`: agrupa endpoints por recurso.
- `Server-src/docker/docker-compose.yml`: levanta PostgreSQL y el contenedor de FastAPI en la misma red.

## Modelo de datos

### CasosSoldadura

Representa parametros de un caso de soldadura:

- `id`: identificador entero autoincremental.
- `Nombre`, `Tiempo`, `Fuerza`, `Compresion`, `Pulsos`, `Material`, `Grosor`, `Separacion`, `Proximidad`.
- `Desalineacion` existe en el modelo ORM, pero actualmente no esta expuesto en el schema HTTP.

### PruebasCETEVI

Representa el resumen de una prueba:

- `Id`: identificador textual primario.
- `Caso`, `Muestras`, `Tiempo`, `FMax`, `IMax`, `Diametro`.

### DatosCETEVI

Representa muestras puntuales de una prueba:

- `id`: identificador entero autoincremental interno.
- `Id`: identificador de prueba.
- `Caso`, `Tiempo`, `Fuerza`, `Corriente`.

## Flujo esperado

1. La GUI crea o consulta casos de soldadura en `/casos`.
2. Durante una prueba, la GUI registra muestras en `/datos`.
3. Al terminar, la GUI registra el resumen de la prueba en `/pruebas`.
4. La API persiste todo en PostgreSQL.

## Notas tecnicas

- La configuracion actual crea tablas al arrancar la aplicacion. Para produccion conviene migrar a Alembic.
- Las credenciales deben venir de `.env`; evita hardcodearlas en codigo.
- La GUI y el servidor deben compartir el contrato de nombres de campos definido en `app/schemas`.
