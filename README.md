# Administrador Flask

Este proyecto es una base para una API REST usando Flask, estructurada por capas y lista para usar con Docker.

## Estructura
- `app.py`: Punto de entrada de la aplicación.
- Carpetas: `models`, `repositories`, `services`, `controllers`, `routes`, `config`.

## Uso rápido

1. Construir y levantar el contenedor:

```bash
docker-compose up --build
```

2. Acceder a la API en [http://localhost:5000](http://localhost:5000)

## Requisitos
- Docker
- Docker Compose 