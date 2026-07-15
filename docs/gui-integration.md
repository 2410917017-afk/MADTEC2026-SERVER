# Integracion con la GUI

La GUI debe tratar al server como un servicio HTTP independiente. El valor central a configurar del lado GUI es la URL base de la API.

## URL base

En desarrollo local con Docker:

```text
http://localhost:8000
```

Si la GUI corre en otra maquina, usa la IP o hostname del equipo que ejecuta el server:

```text
http://<ip-del-servidor>:8000
```

## Contratos usados por la GUI

La GUI debe enviar JSON con los mismos nombres de campos definidos por los schemas:

- Casos: `Nombre`, `Tiempo`, `Fuerza`, `Compresion`, `Pulsos`, `Material`, `Grosor`, `Separacion`, `Proximidad`.
- Pruebas: `Id`, `Caso`, `Muestras`, `Tiempo`, `FMax`, `IMax`, `Diametro`.
- Datos: `Id`, `Caso`, `Tiempo`, `Fuerza`, `Corriente`.

Los nombres actuales usan mayusculas iniciales. Si se decide migrar a nombres estilo `snake_case`, hay que actualizar al mismo tiempo server y GUI.

## Secuencia recomendada

1. Al iniciar, validar `GET /`.
2. Cargar casos con `GET /casos/`.
3. Crear o actualizar casos con `POST /casos/` y `PUT /casos/{id}`.
4. Durante adquisicion, enviar muestras a `POST /datos/`.
5. Al cerrar una prueba, guardar el resumen en `POST /pruebas/`.

## Errores que la GUI debe manejar

- API no disponible: mostrar que el servidor no esta conectado.
- `422`: el payload no coincide con el contrato esperado.
- `404`: el caso solicitado ya no existe.
- Timeout de red: permitir reintentar sin cerrar la aplicacion.
