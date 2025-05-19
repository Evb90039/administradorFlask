"""Archivo principal de la aplicación Flask."""
import logging
import os
from flask import Flask
from routes.guardar import guardar_bp

app = Flask(__name__)

# Configuración básica de seguridad
app.config.update(
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    PERMANENT_SESSION_LIFETIME=1800  # 30 minutos
)

# Configuración de logging
if not logging.getLogger().hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logging.getLogger().addHandler(handler)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

# Configurar logging para usar los handlers de Gunicorn si están disponibles
try:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    if gunicorn_logger.handlers:
        logging.getLogger().handlers = gunicorn_logger.handlers
        logging.getLogger().setLevel(gunicorn_logger.level)
except AttributeError as e:
    logging.warning("No se pudo configurar el logger de Gunicorn: %s", e)

# Registrar blueprints
app.register_blueprint(guardar_bp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    debug = os.environ.get("FLASK_ENV", "production") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)
