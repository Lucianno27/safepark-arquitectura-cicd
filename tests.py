# tests.py
import unittest
from repository import EstacionamientoRepository, Estacionamiento

class EstacionamientoRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.repo = EstacionamientoRepository()
        self.estacionamiento = Estacionamiento(
            id=1,
            direccion="Av. Universidad 123",
            precio_por_hora=1500.0,
            estado="DISPONIBLE"
        )
        self.repo.guardar(self.estacionamiento)

    def test_obtener_por_id(self):
        resultado = self.repo.obtener_por_id(1)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.direccion, "Av. Universidad 123")

    def test_actualizar_estado(self):
        exito = self.repo.actualizar_estado(1, "OCUPADO")
        self.assertTrue(exito)
        actualizado = self.repo.obtener_por_id(1)
        self.assertEqual(actualizado.estado, "OCUPADO")

if __name__ == '__main__':
    unittest.main()