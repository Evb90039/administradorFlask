from flask import Blueprint, request
from controllers.guardar_controller import guardar

guardar_bp = Blueprint('guardar', __name__, url_prefix='/guardar')

@guardar_bp.route('/', methods=['POST'])
def guardar_route():
    return guardar(request) 
