def create_matrix():
    """Crea una matriz de 5x8 inicializada con ceros."""
    rows, cols = 5, 8
    return [[0 for _ in range(rows)] for _ in range(cols)]

class Player:
    def __init__(self, name: str):
        self.name = name
        self.total_ships = 3
        self.ships_in_game = 0
        self.remaining_shots = 1
        self.board = create_matrix()
        self.board_attack = None

def convert_location(position: str) -> tuple:
    """Convierte una posición en el formato A1 a coordenadas de matriz."""
    try:
        column_mapping = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}
        column = position[0].upper()
        row = int(position[1])

        if column in column_mapping and 1 <= row <= 8:
            return column_mapping[column] - 1, row - 1  # Ajuste para índices de matriz
        raise ValueError(f"Posición fuera de rango: {position}")
    except (IndexError, ValueError) as e:
        raise ValueError(f"Formato inválido de la posición '{position}': {e}")

class NavalWarfare:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1
        self.is_victory = False

    def place_ship(self, ship_position: str):
        """Posiciona un barco en el tablero del jugador actual."""
        try:
            col, row = convert_location(ship_position)
            if 0 <= col < 5 and 0 <= row < 8:
                if self.current_player.board[row][col] == 0:
                    self.current_player.total_ships -= 1
                    self.current_player.ships_in_game += 1
                    self.current_player.board[row][col] = 1
                else:
                    raise ValueError("La ubicación ya está ocupada. Elige otra posición.")
            else:
                raise ValueError("Posición fuera de los límites del tablero.")
        except ValueError as e:
            raise ValueError(f"Error al posicionar el barco: {e}")
        except Exception as e:
            raise RuntimeError(f"Error inesperado al colocar barco en '{ship_position}': {e}")

    def shoot(self, target_position: str):
        """Realiza un disparo en la ubicación indicada."""
        try:
            if self.has_remaining_shots():
                col, row = convert_location(target_position)
                if 0 <= col < 5 and 0 <= row < 8:
                    self.current_player.remaining_shots -= 1
                    
                    if self.current_player.board_attack[row][col] == 1:
                        return self.register_hit(col, row)
                    else:
                        self.current_player.board_attack[row][col] = -1  # Marca como agua
                        return False
                else:
                    raise ValueError("Posición fuera de los límites del tablero.")
            else:
                raise ValueError("No tienes intentos disponibles.")
        except ValueError as e:
            raise ValueError(f"Error al realizar el disparo: {e}")
        except Exception as e:
            raise RuntimeError(f"Error inesperado durante el disparo en '{target_position}': {e}")

    def register_hit(self, col: int, row: int):
        """Registra un golpe en el tablero y reduce los barcos en juego del oponente."""
        try:
            self.current_player.board_attack[row][col] = 2  # Marca como golpeado
            if self.current_player == self.player1:
                self.player2.ships_in_game -= 1
            else:
                self.player1.ships_in_game -= 1
            return True
        except Exception as e:
            raise RuntimeError(f"Error al registrar golpe en [{row}, {col}]: {e}")

    def has_remaining_shots(self):
        """Verifica si el jugador actual tiene intentos restantes."""
        try:
            return self.current_player.remaining_shots > 0
        except Exception as e:
            raise RuntimeError(f"Error al verificar los intentos restantes: {e}")

    def switch_player(self):
        """Cambia el turno al otro jugador."""
        try:
            self.current_player = self.player2 if self.current_player == self.player1 else self.player1
            if self.current_player.remaining_shots == 0:
                self.current_player.remaining_shots = 1
        except Exception as e:
            raise RuntimeError(f"Error al cambiar de jugador: {e}")

    def is_game_over(self):
        """Verifica si alguno de los jugadores ha perdido todos sus barcos."""
        try:
            return self.player1.ships_in_game == 0 or self.player2.ships_in_game == 0
        except Exception as e:
            raise RuntimeError(f"Error al verificar si el juego ha terminado: {e}")

    def setup_attack_boards(self):
        """Asigna el tablero de ataque para cada jugador."""
        try:
            self.player1.board_attack = self.player2.board
            self.player2.board_attack = self.player1.board
        except Exception as e:
            raise RuntimeError(f"Error al configurar los tableros de ataque: {e}")
