# API

Base URL por defecto en desarrollo:

```text
http://localhost:8000
```

FastAPI publica la especificacion interactiva en:

```text
http://localhost:8000/docs
```

## Estado

### `GET /`

Devuelve el estado basico del servidor.

Respuesta:

```json
{
  "status": "ok",
  "message": "Servidor funcionando"
}
```

## Casos de soldadura

### `GET /casos/`

Lista todos los casos.

### `GET /casos/{id}`

Consulta un caso por identificador entero.

### `POST /casos/`

Crea un caso.

Payload:

```json
{
  "Nombre": "Caso 1",
  "Tiempo": 1.5,
  "Fuerza": 1200.0,
  "Compresion": 0.3,
  "Pulsos": 2,
  "Material": "Acero",
  "Grosor": 1.2,
  "Separacion": 0.0,
  "Proximidad": 0.0
}
```

### `PUT /casos/{id}`

Actualiza un caso completo.

### `DELETE /casos/{id_caso}`

Elimina un caso.

## Pruebas

### `GET /pruebas/`

Lista todos los resumenes de pruebas.

### `POST /pruebas/`

Crea un resumen de prueba.

Payload:

```json
{
  "Id": "P-001",
  "Caso": "Caso 1",
  "Muestras": 100,
  "Tiempo": 1.5,
  "FMax": 1200.0,
  "IMax": 8500.0,
  "Diametro": 4.2
}
```

## Datos

### `GET /datos/`

Lista todas las muestras registradas.

### `POST /datos/`

Crea una muestra.

Payload:

```json
{
  "Id": "P-001",
  "Caso": "Caso 1",
  "Tiempo": 0.12,
  "Fuerza": 950.0,
  "Corriente": 7200.0
}
```

## Codigos de error relevantes

- `404`: recurso no encontrado, por ejemplo al consultar o eliminar un caso inexistente.
- `422`: payload invalido segun los schemas Pydantic.
- `500`: error interno, comunmente por conexion fallida a la base de datos.
