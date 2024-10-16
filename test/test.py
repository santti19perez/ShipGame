import unittest
import sys
sys.path.append("src")
from Logic.NavalWarfare2 import NavalWarfare, Player, convert_location

class TestNavalWarfareSuccess(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Jugador1")
        self.player2 = Player("Jugador2")
        self.game = NavalWarfare(self.player1, self.player2)

    def test_place_ship_success(self):
        """Prueba colocar un barco exitosamente."""
        self.game.place_ship("A1")
        self.assertEqual(self.player1.board[0][0], 1)

    def test_switch_player(self):
        """Prueba cambiar de jugador."""
        self.game.switch_player()
        self.assertEqual(self.game.current_player, self.player2)

    def test_shoot_successful_hit(self):
        """Prueba un disparo exitoso que impacta un barco."""
        self.player2.board[0][0] = 1
        self.game.setup_attack_boards()
        result = self.game.shoot("A1")
        self.assertTrue(result)

    def test_shoot_miss(self):
        """Prueba un disparo fallido."""
        self.game.setup_attack_boards()
        result = self.game.shoot("A1")
        self.assertFalse(result)

    def test_game_over_condition(self):
        """Prueba la condición de final del juego."""
        self.player2.ships_in_game = 0
        self.assertTrue(self.game.is_game_over())

    def test_remaining_shots(self):
        """Prueba que el jugador tiene intentos restantes."""
        self.assertTrue(self.game.has_remaining_shots())

    def test_convert_location(self):
        """Prueba convertir una ubicación en coordenadas de matriz."""
        result = convert_location("A1")
        self.assertEqual(result, (0, 0))


#Test valores Extremos

class TestNavalWarfareExtreme(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Jugador1")
        self.player2 = Player("Jugador2")
        self.game = NavalWarfare(self.player1, self.player2)

    def test_place_ship_edge_top_right(self):
        """Prueba colocar un barco en la esquina superior derecha."""
        self.game.place_ship("E1")
        self.assertEqual(self.player1.board[0][4], 1)

    def test_place_ship_edge_bottom_left(self):
        """Prueba colocar un barco en la esquina inferior izquierda."""
        self.game.place_ship("A8")
        self.assertEqual(self.player1.board[7][0], 1)

    def test_convert_location_top_left(self):
        """Prueba convertir la esquina superior izquierda."""
        result = convert_location("A1")
        self.assertEqual(result, (0, 0))

    def test_convert_location_bottom_right(self):
        """Prueba convertir la esquina inferior derecha."""
        result = convert_location("E8")
        self.assertEqual(result, (4, 7))

    def test_shoot_edge_position(self):
        """Prueba disparar en el borde del tablero."""
        self.game.setup_attack_boards()
        result = self.game.shoot("E8")
        self.assertFalse(result)

    def test_place_ship_max_ships(self):
        """Prueba colocar el máximo número de barcos."""
        self.game.place_ship("A1")
        self.game.place_ship("B1")
        self.game.place_ship("C1")
        self.assertEqual(self.player1.ships_in_game, 3)

    def test_remaining_shots_at_max(self):
        """Prueba que el jugador tiene el número máximo de disparos restantes."""
        self.assertEqual(self.player1.remaining_shots, 1)

#Test Fallidos

class TestNavalWarfareFailure(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Jugador1")
        self.player2 = Player("Jugador2")
        self.game = NavalWarfare(self.player1, self.player2)

    def test_invalid_position_out_of_range(self):
        """Prueba colocar un barco en una posición fuera de rango."""
        with self.assertRaises(ValueError):
            self.game.place_ship("F1")  # 'F' no es válido

    def test_invalid_position_numeric_out_of_range(self):
        """Prueba colocar un barco en una posición con número fuera de rango."""
        with self.assertRaises(ValueError):
            self.game.place_ship("A9")  # '9' no es válido

    def test_place_ship_on_occupied_space(self):
        """Prueba colocar un barco en un espacio ocupado."""
        self.game.place_ship("A1")
        with self.assertRaises(ValueError):
            self.game.place_ship("A1")  # Mismo lugar ocupado

    def test_shoot_without_shots_left(self):
        """Prueba disparar cuando no quedan intentos."""
        self.game.setup_attack_boards()
        self.game.current_player.remaining_shots = 0
        with self.assertRaises(ValueError):
            self.game.shoot("A1")

    def test_invalid_shoot_position(self):
        """Prueba disparar en una posición fuera de rango."""
        self.game.setup_attack_boards()
        with self.assertRaises(ValueError):
            self.game.shoot("F1")

    def test_convert_invalid_location(self):
        """Prueba convertir una ubicación inválida."""
        with self.assertRaises(ValueError):
            convert_location("Z1")  # 'Z' no es una letra válida

    def test_no_ships_remaining(self):
        """Prueba disparar cuando no quedan barcos del oponente."""
        self.player2.ships_in_game = 0
        self.assertTrue(self.game.is_game_over())

if __name__ == '__main__':
    unittest.main()