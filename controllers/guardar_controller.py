"""Controlador para la lógica de guardado."""
import logging
from flask import jsonify
from decorators.decorators import require_json
from services.guardar_service import guardar_en_firebase
from models.guardar_model import GuardarModel

@require_json
def guardar(data):
    """Procesa y guarda los datos recibidos en la petición."""
    logging.info("Entrando a la función guardar con data: %s", data)
    guardar_data = GuardarModel(**data)
    print('Intento de guardar:', guardar_data)

    if not guardar_data.is_valid():
        print('Faltan campos requeridos o tipos incorrectos:', guardar_data)
        return jsonify({'error': 'Faltan campos requeridos o tipos incorrectos'}), 400
    try:
        doc_id = guardar_en_firebase(guardar_data)
        print('Guardado correctamente, ID:', doc_id)
        return jsonify({'id': doc_id, 'message': 'Guardado correctamente'})
    except ValueError as error:
        print('Error al guardar en Firebase:', str(error))
        return jsonify({'error': 'Error al guardar en Firebase', 'details': str(error)}), 500
