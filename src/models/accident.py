

class Accidente:
    def __init__(self, id_accidente, fecha, lugar, descripcion):
        self.id_accidente = id_accidente
        self.fecha = fecha
        self.lugar = lugar
        self.descripcion = descripcion

    def to_dict(self):
        """Convierte el objeto a un diccionario."""
        return {
            'idAccidente': self.id_accidente,
            'fecha': self.fecha,
            'lugar': self.lugar,
            'descripcion': self.descripcion
        }
