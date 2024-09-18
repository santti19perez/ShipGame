import unittest
from board import update_board
from functions import input_to_coords

class TestGame(unittest.TestCase):
    
    def test_input_to_coords(self):
        self.assertEqual(input_to_coords('D2'), (1, 3))
        self.assertEqual(input_to_coords('A1'), (0, 0))
        self.assertEqual(input_to_coords('E5'), (4, 4))
        self.assertEqual(input_to_coords('F6'), (None, None))
    
    def test_update_board(self):
        board = [[' ' for _ in range(5)] for _ in range(5)]
        self.assertTrue(update_board(board, 0, 0))
        self.assertFalse(update_board(board, 0, 0))

if __name__ == "__main__":
    unittest.main()
