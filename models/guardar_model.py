class GuardarModel:
    def __init__(self, Nombre=None, apellido=None, ahorro=None):
        self.Nombre = Nombre
        self.apellido = apellido
        self.ahorro = ahorro

    def is_valid(self):
        return all([
            isinstance(self.Nombre, str) and self.Nombre.strip(),
            isinstance(self.apellido, str) and self.apellido.strip(),
            isinstance(self.ahorro, (int, float)),
        ]) 