def print_board(board, hide_ships=False, owner=""):
    print("No use los formatos incorrectos como (c11, 4a). Usa el formato correcto (e.j., D2).")
    print(f"Tablero de {owner}, encuentra su barco")
    print("    A   B   C   D   E")
    print("  +---+---+---+---+---+")
    for i, row in enumerate(board, start=1):
        row_display = [' ' if cell == 'S' and hide_ships else cell for cell in row]
        print(f"{i} | {' | '.join(row_display)} |")
        print("  +---+---+---+---+---+")

def update_board(board, row, col):
    if board[row][col] == ' ':
        board[row][col] = 'S'
        return True
    else:
        from errors import position_occupied_error
        position_occupied_error()
        return False

def hide_ships(board, player):
    from functions import clear_screen, input_to_coords
    for _ in range(5):
        while True:
            clear_screen()
            print_board(board, hide_ships=True)
            print(f"{player}, esconde tu barco (e.j., D2):")
            ship_input = input()
            ship_row, ship_col = input_to_coords(ship_input)
            if ship_row is not None and ship_col is not None and update_board(board, ship_row, ship_col):
                break
