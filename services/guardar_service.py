"""Servicio para la lógica de guardado en Firebase."""
from repositories.guardar_repository import guardar

def guardar_en_firebase(guardar_data):
    """Guarda los datos en Firebase."""
    return guardar(guardar_data)
