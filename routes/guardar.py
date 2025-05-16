"""Rutas para los endpoints de guardar."""
import logging
from flask import Blueprint, request
from controllers.guardar_controller import guardar


guardar_bp = Blueprint('guardar', __name__, url_prefix='/guardar')
guardar_bp.add_url_rule('/', view_func=guardar, methods=['POST'])

@guardar_bp.route('/', methods=['POST'])
def guardar_route():
    """Endpoint para guardar datos mediante POST."""
    logging.error("PRUEBA: Este es un error desde el route")
    return guardar(request.get_json(force=True))
