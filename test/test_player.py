# Archivo: test/test_jugador.py

import sys
sys.path.append("src")

import unittest
from model.player_model import Jugador
from db_connection import get_connection

class TestJugadorModelo(unittest.TestCase):
    def setUp(self):
        # aqui se limpia la base de datos
        self.limpiar_base_de_datos()

    def limpiar_base_de_datos(self):
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            try:
                
                cursor.execute("DELETE FROM tableros;")
           
                cursor.execute("DELETE FROM juegos;")
                cursor.execute("DELETE FROM jugadores;")
                connection.commit()
            except Exception as e:
                print(f"Error al limpiar la base de datos: {e}")
            finally:
                cursor.close()
                connection.close()

    def test_crear_jugador_exitoso(self):
        jugador = Jugador(nombre="JugadorPrueba")
        jugador_creado = jugador.crear()
        self.assertIsNotNone(jugador_creado)
        self.assertIsNotNone(jugador_creado.id)
        self.assertEqual(jugador_creado.nombre, "JugadorPrueba")

    def test_crear_jugador_error(self):
        jugador = Jugador(nombre="")
        jugador_creado = jugador.crear()
        self.assertIsNone(jugador_creado)

    def test_actualizar_jugador_exitoso(self):
        jugador = Jugador(nombre="JugadorActualizar")
        jugador.crear()
        resultado = jugador.actualizar("NuevoNombre")
        self.assertTrue(resultado)
        jugador_actualizado = Jugador.obtener_por_id(jugador.id)
        self.assertEqual(jugador_actualizado.nombre, "NuevoNombre")

    def test_actualizar_jugador_error(self):
        jugador = Jugador(id=9999)
        resultado = jugador.actualizar("NombreInexistente")
        self.assertFalse(resultado)

    def test_eliminar_jugador_exitoso(self):
        jugador = Jugador(nombre="JugadorEliminar")
        jugador.crear()
        resultado = jugador.eliminar()
        self.assertTrue(resultado)
        jugador_eliminado = Jugador.obtener_por_id(jugador.id)
        self.assertIsNone(jugador_eliminado)

    def test_eliminar_jugador_error(self):
        jugador = Jugador(id=9999)
        resultado = jugador.eliminar()
        self.assertFalse(resultado)

    def test_obtener_jugador_no_existente(self):
        jugador = Jugador.obtener_por_id(9999)
        self.assertIsNone(jugador)

if __name__ == '__main__':
    unittest.main()
