"""Repositorio para operaciones de guardado en Firestore."""
from config.firebase import db

def guardar(guardar_data):
    """Guarda los datos en la colección 'pruebaback' de Firestore."""
    doc_ref = db.collection('pruebaback').add({
        'nombre': guardar_data.nombre,
        'apellido': guardar_data.apellido,
        'ahorro': guardar_data.ahorro
    })
    return doc_ref[1].id  # add() retorna (update_time, ref)
