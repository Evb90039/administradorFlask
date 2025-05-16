"""Modelo para validar y almacenar datos de guardado."""
class GuardarModel:
    """Modelo para validar y almacenar datos de guardado."""
    def __init__(self, nombre=None, apellido=None, ahorro=None):
        self.nombre = nombre
        self.apellido = apellido
        self.ahorro = ahorro

    def is_valid(self):
        """Valida los campos del modelo GuardarModel."""
        return all([
            isinstance(self.nombre, str) and self.nombre.strip(),
            isinstance(self.apellido, str) and self.apellido.strip(),
            isinstance(self.ahorro, (int, float)),
        ])

    def to_dict(self):
        """Convierte el modelo a un diccionario."""
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "ahorro": self.ahorro,
        }

    def __repr__(self):
        return f"GuardarModel(nombre={self.nombre}, apellido={self.apellido}, ahorro={self.ahorro})"
