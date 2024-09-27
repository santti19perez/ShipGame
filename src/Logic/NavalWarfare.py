def create_matrix():
    w, h = 5, 8
    matrix = [[0 for x in range(w)] for j in range(h)]
    return matrix


class Player:
    def __init__(self, name: str):
        self.name = name
        self.ships: int = 3
        self.ships_in_game = 0
        self.trys: int = 1
        self.board = create_matrix()
        self.board_attack = None


def convert_location(position: str) -> tuple:
    letras = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}
    letra = position[0].upper()
    fila = int(position[1])
    if letra in letras:
        location = (letras[letra] - 1, fila - 1)  # Ajuste para índices de matriz
        return location


class NavalWarfare:
    def __init__(self, player1: Player, player2: Player, score_file: str = "scores.txt"):
        self.Player1 = player1
        self.Player2 = player2
        self.currentplayer = self.Player1
        self.score_file = score_file
        self.Victoria = False
      
    def posicionate_ship(self, location_ship: str):
        try:
            letra, fila = convert_location(location_ship)
            self.currentplayer.ships -= 1
            self.currentplayer.ships_in_game += 1
            self.currentplayer.board[fila][letra] = 1
        except:
            raise ValueError("No se puede posicionar el barco aquí. Elige otra ubicación.")

    def shoot(self, location: str):
        if self.verify_trys():
            letra, fila = convert_location(location)
            self.currentplayer.trys -= 1  # Reduce el número de intentos
            if self.currentplayer.board_attack[fila][letra] == 1:
                return self.hit(letra, fila)
            
            else:
                self.currentplayer.board_attack[fila][letra] = -1  # Marca como agua
                return False
        else:
            raise ValueError("No hay intentos disponibles")

    def hit(self, y, x):
        self.currentplayer.board_attack[x][y] = 2  # Marca como golpeado
        if self.currentplayer.name == self.Player1.name:
            self.Player2.ships_in_game -= 1
            print(f"jugador 2 {self.Player2.ships_in_game}")
        else:
            self.Player1.ships_in_game -= 1
            print(f"jugador 1 {self.Player1.ships_in_game}") 
        return True

    def verify_trys(self):
        if self.currentplayer.trys > 0:
            return True
        else:
            return False

    def update_current_player(self):
        if self.currentplayer == self.Player2:
            self.currentplayer = self.Player1
            if self.currentplayer.trys == 0:
                self.currentplayer.trys += 1

        else: 
            self.currentplayer = self.Player2
            if self.currentplayer.trys == 0:
                self.currentplayer.trys += 1
        return self.currentplayer

    def game_over(self):
        if self.Player1.ships_in_game == 0 or self.Player2.ships_in_game == 0:
                return True
        else:
            return False
        
    def attack_board(self):
        self.Player1.board_attack = self.Player2.board
        self.Player2.board_attack = self.Player1.board
        return