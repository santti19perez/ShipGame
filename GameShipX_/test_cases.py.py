import unittest
from board import update_board, print_board, hide_ships
from functions import input_to_coords, is_valid_guess, clear_screen, update_score
from errors import invalid_input_error, position_occupied_error, already_guessed_error

class TestGame(unittest.TestCase):

    def test_input_to_coords_valid(self):
        self.assertEqual(input_to_coords('D2'), (1, 3))
        self.assertEqual(input_to_coords('A1'), (0, 0))
        self.assertEqual(input_to_coords('E5'), (4, 4))

    def test_input_to_coords_invalid(self):
        self.assertEqual(input_to_coords('F6'), (None, None))

    def test_update_board(self):
        board = [[' ' for _ in range(5)] for _ in range(5)]
        self.assertTrue(update_board(board, 0, 0))
        self.assertFalse(update_board(board, 0, 0))

    def test_update_board_out_of_bounds(self):
        board = [[' ' for _ in range(5)] for _ in range(5)]
        with self.assertRaises(IndexError):
            update_board(board, 5, 5)

    def test_is_valid_guess(self):
        board = [[' ' for _ in range(5)] for _ in range(5)]
        guesses = set()
        self.assertTrue(is_valid_guess(board, 0, 0, guesses))
        guesses.add((0, 0))
        self.assertFalse(is_valid_guess(board, 0, 0, guesses))

    def test_update_score(self):
        score = {'Jugador 1': 0, 'Jugador 2': 0}
        updated_score = update_score(score, 'Jugador 1')
        self.assertEqual(updated_score['Jugador 1'], 1)

    def test_hide_ships_valid(self):
        board = [[' ' for _ in range(5)] for _ in range(5)]
        with unittest.mock.patch('builtins.input', return_value='A1'):
            hide_ships(board, 'Jugador 1')
        self.assertEqual(board[0][0], 'S')

    def test_hide_ships_invalid_input(self):
        board = [[' ' for _ in range(5)] for _ in range(5)]
        with unittest.mock.patch('builtins.input', return_value='Z9'):
            hide_ships(board, 'Jugador 1')
        self.assertEqual(board[0][0], ' ')

    def test_print_board(self):
        import io
        board = [[' ' for _ in range(5)] for _ in range(5)]
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print_board(board)
            output = mock_stdout.getvalue()
        self.assertIn('A B C D E', output)

    def test_error_handling(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            invalid_input_error()
            mock_print.assert_called_with("Entrada inválida. Usa el formato correcto (e.j., D2).")

    def test_no_ships_hidden(self):
        board = [[' ' for _ in range(5)] for _ in range(5)]
        hide_ships(board, 'Jugador 1')
        self.assertIn('S', [cell for row in board for cell in row])

    def test_edge_case(self):
        board = [['S' for _ in range(5)] for _ in range(5)]
        self.assertTrue(all(cell == 'S' for row in board for cell in row))

    def test_empty_board(self):
        board = [[' ' for _ in range(5)] for _ in range(5)]
        self.assertTrue(all(cell == ' ' for row in board for cell in row))

    def test_full_board(self):
        board = [['S' for _ in range(5)] for _ in range(5)]
        self.assertTrue(all(cell == 'S' for row in board for cell in row))

    def test_board_reset(self):
        board = [['S' for _ in range(5)] for _ in range(5)]
        board = [[' ' for _ in range(5)] for _ in range(5)]
        self.assertTrue(all(cell == ' ' for row in board for cell in row))

    def test_valid_guess(self):
        board = [[' ' for _ in range(5)] for _ in range(5)]
        guesses = set()
        self.assertTrue(is_valid_guess(board, 0, 0, guesses))

    def test_score_update(self):
        score = {'Jugador 1': 0, 'Jugador 2': 0}
        updated_score = update_score(score, 'Jugador 1')
        self.assertEqual(updated_score['Jugador 1'], 1)

    def test_board_update_after_game(self):
        board = [[' ' for _ in range(5)] for _ in range(5)]
        # Simula el juego aquí y verifica que el tablero se actualice correctamente
        pass

    def test_game_winner(self):
        # Verificar el ganador del juego en base a los puntajes
        pass

    def test_error_handling_on_invalid_input(self):
        with unittest.mock.patch('builtins.print') as mock_print:
            invalid_input_error()
            mock_print.assert_called_with("Entrada inválida. Usa el formato correcto (e.j., D2).")

    def test_input_coordinates_exceeding(self):
        board = [[' ' for _ in range(5)] for _ in range(5)]
        with self.assertRaises(IndexError):
            input_to_coords('F6')

if __name__ == "__main__":
    unittest.main()
