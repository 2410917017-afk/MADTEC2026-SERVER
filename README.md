# MADTEC2026 Server

Backend FastAPI para registrar y consultar datos de pruebas de soldadura del laboratorio CETEVI-UAQ.

El repositorio contiene solamente el servidor y la base de datos. La GUI vive en un repositorio separado y consume esta API por HTTP.

## Estructura

```text
Server-src/
  backend/
    app/
      main.py              # Entrada FastAPI
      database/            # Conexion SQLAlchemy
      models/              # Modelos ORM
      routers/             # Endpoints HTTP
      schemas/             # Esquemas Pydantic
    Dockerfile
    requirements.txt
  docker/
    docker-compose.yml     # PostgreSQL + API
    postgres/init.sql
docs/
```

## Requisitos

- Docker y Docker Compose para levantar el entorno completo.
- Python 3.10+ si se ejecuta el backend sin contenedores.

## Configuracion

Copia los ejemplos de entorno y ajusta los valores si hace falta:

```bash
cp Server-src/docker/.env.example Server-src/docker/.env
cp Server-src/backend/.env.example Server-src/backend/.env
```

La API usa `DATABASE_URL`. En Docker, el host de PostgreSQL debe ser `postgres` porque ese es el nombre del servicio en `docker-compose.yml`.

## Ejecutar con Docker

```bash
cd Server-src/docker
docker compose up --build
```

Servicios expuestos:

- API: `http://localhost:8000`
- Swagger/OpenAPI: `http://localhost:8000/docs`
- PostgreSQL: `localhost:5432`

## Ejecutar localmente

Primero levanta PostgreSQL o apunta `DATABASE_URL` a una base disponible:

```bash
cd Server-src/backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
## Modificar ruta de almacenamiento
Si se desea modificar la ruta de almacenamiento para el servidor se debe modificar el contenido del apartado `volumes:` en el archivo `Server-src/docker/docker-compose.yml`
- Para guardar imagenes se podría crear una carpeta `app/images/` y se programa para guardar ahí las imagenes que llegan a la API. Y en `volumes` se agrega:

```yml
 volumes:
   - "ruta del disco duro" : /app/images
```

- Para guardar las tablas de datos de Postgre, se reemplaza la línea:

```yml
volumes:
  - ./postgres/data:/var/lib/postgresql/data
```
por

```yml
 volumes:
   - "ruta del disco duro":/var/lib/postgresql/data
```


## Documentacion

- [Arquitectura](docs/architecture.md)
- [API](docs/api.md)
- [Despliegue](docs/deployment.md)
- [Integracion con GUI](docs/gui-integration.md)
