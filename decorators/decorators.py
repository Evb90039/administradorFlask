"""Decoradores personalizados"""
from functools import wraps
from flask import request, jsonify
from werkzeug.exceptions import BadRequest

def require_json(f):
    """Decorator que valida que la petición tenga un JSON válido y no vacío."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            data = request.get_json(force=True)
        except BadRequest as e:
            print('JSON inválido:', str(e))
            return jsonify({'error': 'JSON inválido', 'details': str(e)}), 400
        if not data:
            print('No se recibió JSON o está vacío')
            return jsonify({'error': 'No se recibió JSON o está vacío'}), 400

        return f(data, *args, **kwargs)
    return decorated_function
