# Dockerfile para Flask en AWS App Runner
FROM python:3.10-slim

# Crear usuario no root
RUN useradd -m -u 1000 appuser

WORKDIR /app

# Copiar solo requirements.txt primero para aprovechar la caché de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Cambiar permisos y usuario
RUN chown -R appuser:appuser /app
USER appuser

# Exponer el puerto que usa AWS App Runner
EXPOSE 8080

# Usar variables de entorno para configuración
ENV PORT=8080
ENV HOST=0.0.0.0

# Comando para iniciar la aplicación
CMD gunicorn app:app --bind ${HOST}:${PORT} --workers 2 --threads 2 --timeout 0 --capture-output --log-level info 