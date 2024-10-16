import sys
sys.path.append("src")
from Logic.NavalWarfare import NavalWarfare, Player


class InvalidPositionError(Exception):
    """Excepción personalizada para posiciones inválidas."""
    def __init__(self, position, message):
        super().__init__(message)
        self.position = position

    def __str__(self):
        return f"Error de posicionamiento: intentaste posicionar en '{self.position}'. {self.args[0]}"


class GameOverError(Exception):
    """Excepción personalizada para indicar que el juego ha terminado."""
    def __init__(self, message):
        super().__init__(message)


def validate_position_in_range(position, max_letters=5, max_numbers=8):
    """Valida que la posición ingresada esté dentro de los límites del tablero."""
    letras = "ABCDE"
    try:
        letra = position[0].upper()
        numero = int(position[1])

        if letra not in letras or not (1 <= numero <= max_numbers):
            raise InvalidPositionError(position, f"El rango válido de las letras es A-{letras[max_letters-1]} y los números deben estar entre 1-{max_numbers}.")
    except (IndexError, ValueError):
        raise InvalidPositionError(position, "Formato inválido. Asegúrate de ingresar la posición en el formato correcto (ej: A1).")


def imprimir_tablero(matrix):
    """Imprime el tablero completo."""
    letras = "ABCDE"
    encabezado = "  " + " ".join(letras[:len(matrix[0])])
    filas = [f"{idx + 1} " + " ".join(str(cell) for cell in row) for idx, row in enumerate(matrix)]
    print(encabezado)
    print("\n".join(filas))


def imprimir_tablero_oculto(matrix):
    """Imprime el tablero oculto (sin mostrar barcos)."""
    letras = "ABCDE"
    encabezado = "  " + " ".join(letras[:len(matrix[0])])
    filas_ocultas = [
        f"{idx + 1} " + " ".join(["2" if cell == 2 else "-1" if cell == -1 else "0" for cell in row])
        for idx, row in enumerate(matrix)
    ]
    print(encabezado)
    print("\n".join(filas_ocultas))


def pedir_y_validar_posicion(mensaje):
    """Solicita al jugador una posición y la valida."""
    while True:
        try:
            posicion = input(mensaje)
            validate_position_in_range(posicion)
            return posicion
        except InvalidPositionError as e:
            print(f"{e}. El rango válido de las letras es A-E y los números deben estar entre 1-8.")
        except ValueError as e:
            print(f"Posición inválida: '{e}'. Asegúrate de ingresar el formato correcto (ej: A1) con letras entre A-E y números entre 1-8.")


def colocar_barcos(juego):
    """Fase de colocación de barcos."""
    for _ in range(2):
        print(f"///////////////////////////////////////////")
        print(f"Tablero del jugador {juego.current_player.name}")
        imprimir_tablero(juego.current_player.board)

        while juego.current_player.total_ships > 0:
            ship_position = pedir_y_validar_posicion("Ingrese una locación para posicionar su barco (ej: A1): ")
            juego.place_ship(ship_position)
            imprimir_tablero(juego.current_player.board)

        juego.switch_player()


def fase_ataque(juego):
    """Fase de ataque entre jugadores."""
    while not juego.is_game_over():
        print(f"Comienza atacando el jugador {juego.current_player.name}")
        imprimir_tablero_oculto(juego.current_player.board_attack)

        attack_position = pedir_y_validar_posicion(f"Jugador {juego.current_player.name}, ingrese una locación para atacar (ej: A1): ")
        if juego.shoot(attack_position):
            print(f"¡Le has dado a un barco!")
        else:
            print(f"¡Has fallado!")

        imprimir_tablero_oculto(juego.current_player.board_attack)

        if juego.is_game_over():
            raise GameOverError("El juego ha terminado.")
            
        juego.switch_player()


def main():
    try:
        player1 = Player(input("Ingrese el nombre del jugador 1: "))
        player2 = Player(input("Ingrese el nombre del jugador 2: "))

        juego = NavalWarfare(player1, player2)

        colocar_barcos(juego)
        juego.setup_attack_boards()
        fase_ataque(juego)

    except GameOverError:
        if juego.player1.ships_in_game > 0 and juego.player2.ships_in_game == 0:
            print(f"¡Ganó el jugador {juego.player1.name}!")
        elif juego.player2.ships_in_game > 0 and juego.player1.ships_in_game == 0:
            print(f"¡Ganó el jugador {juego.player2.name}!")


if __name__ == "__main__":
    main()