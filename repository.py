# repository.py
class Estacionamiento:
    def __init__(self, id, direccion, precio_por_hora, estado="DISPONIBLE"):
        self.id = id
        self.direccion = direccion
        self.precio_por_hora = precio_por_hora
        self.estado = estado

class EstacionamientoRepository:
    def __init__(self):
        self._db = {}

    def guardar(self, estacionamiento):
        self._db[estacionamiento.id] = estacionamiento

    def obtener_por_id(self, est_id):
        return self._db.get(est_id)

    def actualizar_estado(self, est_id, nuevo_estado):
        estacionamiento = self.obtener_por_id(est_id)
        if estacionamiento:
            estacionamiento.estado = nuevo_estado
            return True
        return False