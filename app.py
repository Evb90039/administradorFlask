"""Archivo principal de la aplicación Flask."""
import logging
from flask import Flask
from routes.guardar import guardar_bp

app = Flask(__name__)
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
except Exception as e:
    logging.warning(f"No se pudo configurar el logger de Gunicorn: {e}")

# Registrar blueprints
app.register_blueprint(guardar_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
