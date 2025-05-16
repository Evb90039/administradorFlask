"""Rutas para los endpoints de guardar."""
from flask import Blueprint, request
from controllers.guardar_controller import guardar

guardar_bp = Blueprint('guardar', __name__, url_prefix='/guardar')

@guardar_bp.route('/', methods=['POST'])
def guardar_route():
    """Endpoint para guardar datos mediante POST."""
    return guardar(request)
