from board import print_board, update_board, hide_ships
from functions import clear_screen, input_to_coords, is_valid_guess, update_score

def play_game():
    score = {'Jugador 1': 0, 'Jugador 2': 0}
    boards = {
        'Jugador 1': [[' ' for _ in range(5)] for _ in range(5)],
        'Jugador 2': [[' ' for _ in range(5)] for _ in range(5)]
    }
    guesses = {'Jugador 1': set(), 'Jugador 2': set()}

    hide_ships(boards['Jugador 1'], 'Jugador 1')
    hide_ships(boards['Jugador 2'], 'Jugador 2')

    current_player = 'Jugador 1'
    opponent = 'Jugador 2'

    while True:
        clear_screen()
        print_board(boards[opponent], hide_ships=True, owner=opponent)
        print(f"Score: Jugador 1 - {score['Jugador 1']}, Jugador 2 - {score['Jugador 2']}")
        print(f"{current_player}, adivina la ubicación del barco del oponente (e.j., D2):")
        guess_input = input()
        guess_row, guess_col = input_to_coords(guess_input)

        if guess_row is None or guess_col is None:
            input("Presiona Enter para continuar...")
            continue

        if not is_valid_guess(boards[opponent], guess_row, guess_col, guesses[current_player]):
            input("Presiona Enter para continuar...")
            continue

        guesses[current_player].add((guess_row, guess_col))

        if boards[opponent][guess_row][guess_col] == 'S':
            print(f"{current_player} adivinó correctamente!")
            score = update_score(score, current_player)
            boards[opponent][guess_row][guess_col] = 'X'
        else:
            boards[opponent][guess_row][guess_col] = 'O'
            print("Fallaste!")

        if score[current_player] == 3:
            print(f"{current_player} gana!")
            break

        current_player, opponent = opponent, current_player
        input("Presiona Enter para cambiar de turno...")

if __name__ == "__main__":
    play_game()
