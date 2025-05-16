from flask import jsonify, request
from services.guardar_service import guardar_en_firebase
from models.guardar_model import GuardarModel

def guardar(req):
    data = req.get_json()
    guardar_data = GuardarModel(**data)
    print('Intento de guardar:', guardar_data)

    if not guardar_data.is_valid():
        print('Faltan campos requeridos o tipos incorrectos:', guardar_data)
        return jsonify({'error': 'Faltan campos requeridos o tipos incorrectos'}), 400
    try:
        id = guardar_en_firebase(guardar_data)
        print('Guardado correctamente, ID:', id)
        return jsonify({'id': id, 'message': 'Guardado correctamente'})
    except Exception as error:
        print('Error al guardar en Firebase:', str(error))
        return jsonify({'error': 'Error al guardar en Firebase', 'details': str(error)}), 500 