from config.firebase import db

def guardar(guardar_data):
    doc_ref = db.collection('pruebaback').add({
        'Nombre': guardar_data.Nombre,
        'apellido': guardar_data.apellido,
        'ahorro': guardar_data.ahorro
    })
    return doc_ref[1].id  # add() retorna (update_time, ref) 