# Despliegue

## Docker Compose

El despliegue principal esta en `Server-src/docker/docker-compose.yml` y define:

- `postgres`: base PostgreSQL 17.
- `fastapi`: API construida desde `Server-src/backend/Dockerfile`.

Para levantarlo:

```bash
cd Server-src/docker
docker compose up --build
```

Para detenerlo:

```bash
docker compose down
```

Para detenerlo y borrar datos locales de PostgreSQL:

```bash
docker compose down -v
```

## Variables de entorno

`Server-src/docker/.env` configura PostgreSQL:

```text
POSTGRES_DB=cetevi_1
POSTGRES_USER=admin
POSTGRES_PASSWORD=madtec2025
```

`Server-src/backend/.env` puede configurar la conexion de SQLAlchemy:

```text
DATABASE_URL=postgresql://admin:madtec2025@postgres:5432/cetevi_1
```

## Persistencia

PostgreSQL guarda datos en:

```text
Server-src/docker/postgres/data/
```

Esa carpeta es runtime local y no debe versionarse.

## Verificacion rapida

Con los contenedores activos:

```bash
curl http://localhost:8000/
```

Respuesta esperada:

```json
{"status":"ok","message":"Servidor funcionando"}
```

## Consideraciones

- El Dockerfile usa Python 3.10 slim.
- El contenedor de API espera que PostgreSQL este saludable antes de arrancar.
- Si se ejecuta fuera de Docker, cambia `postgres` por `localhost` o por el host real de la base en `DATABASE_URL`.
