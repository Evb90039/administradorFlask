"""Rutas para los endpoints de guardar."""
import logging
from flask import Blueprint, request
from controllers.guardar_controller import guardar

logging.basicConfig(level=logging.INFO)

guardar_bp = Blueprint('guardar', __name__, url_prefix='/guardar')
guardar_bp.add_url_rule('/', view_func=guardar, methods=['POST'])

@guardar_bp.route('/', methods=['POST'])
def guardar_route():
    """Endpoint para guardar datos mediante POST."""
    logging.info("Este es un mensaje de información")
    logging.error("Este es un mensaje de error")
    print("Mensaje para los logs")
    return guardar(request.get_json(force=True))
