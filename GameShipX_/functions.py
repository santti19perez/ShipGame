def clear_screen():
    print("\n" * 50)

def input_to_coords(input_str):
    col_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
    if len(input_str) < 2 or input_str[0].upper() not in col_map:
        from errors import invalid_input_error
        invalid_input_error()
        return None, None
    try:
        row = int(input_str[1:]) - 1
        col = col_map[input_str[0].upper()]
        if row < 0 or row > 4:
            print("La fila debe estar entre 1 y 5.")
            return None, None
        return row, col
    except (IndexError, ValueError):
        from errors import invalid_input_error
        invalid_input_error()
        return None, None

def is_valid_guess(board, row, col, guesses):
    if (row, col) in guesses:
        from errors import already_guessed_error
        already_guessed_error()
        return False
    if board[row][col] == 'X' or board[row][col] == 'O':
        print("Esa posición ya ha sido adivinada. Intenta de nuevo.")
        return False
    return True

def update_score(score, player):
    score[player] += 1
    return score
