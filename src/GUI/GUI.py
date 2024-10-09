from kivy.app import App  
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView  # Importar ScrollView

# Pantalla para registrar los nombres de los jugadores
class RegisterScreen(Screen):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        self.player1_name_input = TextInput(hint_text="Nombre de Player 1", multiline=False)
        self.player2_name_input = TextInput(hint_text="Nombre de Player 2", multiline=False)
        self.submit_button = Button(text="Guardar Nombres", on_release=self.save_names, size_hint_y=None, height=40)
        
        layout.add_widget(Label(text="Registro de Jugadores", font_size=24))
        layout.add_widget(self.player1_name_input)
        layout.add_widget(self.player2_name_input)
        layout.add_widget(self.submit_button)
        
        scroll_view = ScrollView()  # Crear un ScrollView
        scroll_view.add_widget(layout)  # Añadir el layout al ScrollView
        self.add_widget(scroll_view)  # Añadir el ScrollView a la pantalla
    
    def save_names(self, *args):
        player1_name = self.player1_name_input.text
        player2_name = self.player2_name_input.text
        if player1_name and player2_name:
            self.manager.player1_name = player1_name
            self.manager.player2_name = player2_name
            self.manager.player1_positions = []
            self.manager.player2_positions = []
            self.manager.current = 'player1_hide'

# Pantalla para que Player 1 esconda sus barcos
class Player1HideScreen(Screen):
    def __init__(self, **kwargs):
        super(Player1HideScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=[20, 20, 20, 20])
        self.label = Label(text="", font_size=24)
        self.confirm_button = Button(text="Confirmar y pasar a Player 2", on_release=self.confirm, size_hint_y=None, height=40)
        self.confirm_button.disabled = True
        
        self.position_input = TextInput(hint_text="Posición del barco (1-25)", multiline=False, input_filter='int')
        self.save_button = Button(text="Guardar posición", on_release=self.save_position, size_hint_y=None, height=40)
        
        self.positions_label = Label(text="Posiciones seleccionadas: ")
        self.player1_positions = []
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.position_input)
        self.layout.add_widget(self.save_button)
        self.layout.add_widget(self.positions_label)

        self.matrix_layout = GridLayout(cols=5, rows=5, spacing=10, padding=[0, 0, 0, 0])
        self.matrix_buttons = [Button(text=str(i + 1), font_size=18, size_hint=(None, None), size=(40, 40)) for i in range(25)]
        for button in self.matrix_buttons:
            self.matrix_layout.add_widget(button)

        # Crear ScrollView para la parte superior
        scroll_view = ScrollView(size_hint=(1, None), size=(400, 300))  # Ajusta el tamaño según necesites
        scroll_view.add_widget(self.matrix_layout)

        self.layout.add_widget(scroll_view)  # Añadir ScrollView al layout
        self.layout.add_widget(self.confirm_button)
        
        self.add_widget(self.layout)

    def on_enter(self):
        self.label.text = f"{self.manager.player1_name} esconde sus barcos"
    
    def save_position(self, *args):
        try:
            position = int(self.position_input.text)
            if 1 <= position <= 25 and position not in self.player1_positions:
                self.player1_positions.append(position)
                self.positions_label.text = f"Posiciones seleccionadas: {self.player1_positions}"
                
                # Limpiar el cuadro de texto
                self.position_input.text = ""

                if len(self.player1_positions) == 5:
                    self.confirm_button.disabled = False
                    self.save_button.disabled = True
            else:
                self.positions_label.text = "Posición inválida o ya seleccionada. Intenta de nuevo."
        except ValueError:
            self.positions_label.text = "Ingresa un número válido."

    def confirm(self, *args):
        self.manager.player1_positions = self.player1_positions
        self.manager.current = 'player2_hide'


# Pantalla para que Player 2 esconda sus barcos
class Player2HideScreen(Screen):
    def __init__(self, **kwargs):
        super(Player2HideScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=[20, 20, 20, 20])
        self.label = Label(text="", font_size=24)
        self.confirm_button = Button(text="Listo", on_release=self.confirm, size_hint_y=None, height=40)
        self.confirm_button.disabled = True
        
        self.position_input = TextInput(hint_text="Posición del barco (1-25)", multiline=False, input_filter='int')
        self.save_button = Button(text="Guardar posición", on_release=self.save_position, size_hint_y=None, height=40)
        
        self.positions_label = Label(text="Posiciones seleccionadas: ")
        self.player2_positions = []
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.position_input)
        self.layout.add_widget(self.save_button)
        self.layout.add_widget(self.positions_label)
        
        self.matrix_layout = GridLayout(cols=5, rows=5, spacing=10, padding=[0, 0, 0, 0])
        self.matrix_buttons = [Button(text=str(i + 1), font_size=18, size_hint=(None, None), size=(40, 40)) for i in range(25)]
        for button in self.matrix_buttons:
            self.matrix_layout.add_widget(button)

        scroll_view = ScrollView(size_hint=(1, None), size=(400, 300))  # Ajusta el tamaño según necesites
        scroll_view.add_widget(self.matrix_layout)

        self.layout.add_widget(scroll_view)  # Añadir ScrollView al layout
        self.layout.add_widget(self.confirm_button)
        
        self.add_widget(self.layout)

    def on_enter(self):
        self.label.text = f"{self.manager.player2_name} esconde sus barcos"
    
    def save_position(self, *args):
        try:
            position = int(self.position_input.text)
            if 1 <= position <= 25 and position not in self.player2_positions:
                self.player2_positions.append(position)
                self.positions_label.text = f"Posiciones seleccionadas: {self.player2_positions}"

                # Limpiar el cuadro de texto
                self.position_input.text = ""

                if len(self.player2_positions) == 5:
                    self.confirm_button.disabled = False
                    self.save_button.disabled = True
            else:
                self.positions_label.text = "Posición inválida o ya seleccionada. Intenta de nuevo."
        except ValueError:
            self.positions_label.text = "Ingresa un número válido."

    def confirm(self, *args):
        self.manager.player2_positions = self.player2_positions
        self.manager.current = 'guess'

# Pantalla para que los jugadores adivinen las posiciones
class GuessScreen(Screen):
    def __init__(self, **kwargs):
        super(GuessScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='horizontal', spacing=10, padding=[20, 20, 20, 20])
        left_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_x=0.75)  # Para el tablero y la información
        right_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_x=0.25)  # Para el botón de salir

        self.label = Label(text="", font_size=24)
        self.result_label = Label(text="")
        self.player1_score = 0
        self.player2_score = 0
        self.current_player = 1  # 1 para Player 1, 2 para Player 2
        self.guessed_positions_player1 = []  # Para rastrear posiciones ya adivinadas por Player 1
        self.guessed_positions_player2 = []  # Para rastrear posiciones ya adivinadas por Player 2

        self.selected_guess = None  # Para almacenar la selección del jugador

        self.score_label = Label(text=f"P1: {self.player1_score} | P2: {self.player2_score}", font_size=24)
        self.winner_label = Label(text="", font_size=24)  # Para mostrar al ganador

        left_layout.add_widget(self.label)
        left_layout.add_widget(self.result_label)
        left_layout.add_widget(self.score_label)
        left_layout.add_widget(self.winner_label)

        # Tablero para el Jugador 1
        self.matrix_layout_player1 = GridLayout(cols=5, rows=5, spacing=10, padding=[0, 0, 0, 0])
        self.matrix_buttons_player1 = [Button(text=str(i + 1), font_size=18, size_hint=(None, None), size=(40, 40)) for i in range(25)]
        for i, button in enumerate(self.matrix_buttons_player1):
            button.bind(on_release=lambda btn, pos=i + 1: self.select_guess(pos, btn))  # Selecciona la adivinanza
            self.matrix_layout_player1.add_widget(button)

        # Tablero para el Jugador 2
        self.matrix_layout_player2 = GridLayout(cols=5, rows=5, spacing=10, padding=[0, 0, 0, 0])
        self.matrix_buttons_player2 = [Button(text=str(i + 1), font_size=18, size_hint=(None, None), size=(40, 40)) for i in range(25)]
        for i, button in enumerate(self.matrix_buttons_player2):
            button.bind(on_release=lambda btn, pos=i + 1: self.select_guess(pos, btn))  # Selecciona la adivinanza
            self.matrix_layout_player2.add_widget(button)

        # ScrollView para el Jugador 1
        scroll_view_player1 = ScrollView(size_hint=(1, None), size=(400, 300))
        scroll_view_player1.add_widget(self.matrix_layout_player1)

        # ScrollView para el Jugador 2
        scroll_view_player2 = ScrollView(size_hint=(1, None), size=(400, 300))
        scroll_view_player2.add_widget(self.matrix_layout_player2)

        left_layout.add_widget(scroll_view_player1)  # Añadir ScrollView del Jugador 1 al layout
        left_layout.add_widget(scroll_view_player2)  # Añadir ScrollView del Jugador 2 al layout

        # Botón de salir
        self.quit_button = Button(text="Salir", size_hint_y=None, height=40, on_release=self.quit_game)

        right_layout.add_widget(self.quit_button)  # Añadir botón de salir al layout derecho

        layout.add_widget(left_layout)  # Añadir el layout izquierdo (tableros y etiquetas)
        layout.add_widget(right_layout)  # Añadir el layout derecho (botones)

        self.add_widget(layout)

        # Mostrar el tablero del Jugador 1 y ocultar el del Jugador 2 al inicio
        self.matrix_layout_player2.opacity = 0
        self.matrix_layout_player2.disabled = True

    def on_enter(self):
        self.label.text = f"{self.manager.player1_name} empieza a adivinar."

    def select_guess(self, guess, button):
        """ Método para manejar la selección de una adivinanza usando los botones de la matriz """
        self.selected_guess = guess
        self.make_guess()  # Llama a la función make_guess para procesar la selección
        if self.result_label.text == "¡Acertaste!":
            button.disabled = True  # Deshabilitar el botón si acierta

    def make_guess(self, *args):
        if self.selected_guess is None:
            self.result_label.text = "Selecciona una posición antes de adivinar."
            return

        guess = self.selected_guess

        try:
            if self.current_player == 1:
                # Verificar si la posición ya fue adivinada por el Jugador 1
                if guess in self.guessed_positions_player1:
                    self.result_label.text = "Esta posición ya ha sido adivinada. Intenta con otra."
                    return
                self.guessed_positions_player1.append(guess)  # Marcar la posición como adivinada

                if guess in self.manager.player2_positions:
                    self.result_label.text = "¡Acertaste!"
                    self.player1_score += 1
                else:
                    self.result_label.text = "Fallaste."
                self.score_label.text = f"P1: {self.player1_score} | P2: {self.player2_score}"
            else:
                # Verificar si la posición ya fue adivinada por el Jugador 2
                if guess in self.guessed_positions_player2:
                    self.result_label.text = "Esta posición ya ha sido adivinada. Intenta con otra."
                    return
                self.guessed_positions_player2.append(guess)  # Marcar la posición como adivinada

                if guess in self.manager.player1_positions:
                    self.result_label.text = "¡Acertaste!"
                    self.player2_score += 1
                else:
                    self.result_label.text = "Fallaste."
                self.score_label.text = f"P1: {self.player1_score} | P2: {self.player2_score}"

            # Comprobar ganador
            if self.player1_score >= 5:
                self.winner_label.text = f"¡{self.manager.player1_name} gana!"
                self.disable_all_buttons()  # Deshabilitar todos los botones del tablero
            elif self.player2_score >= 5:
                self.winner_label.text = f"¡{self.manager.player2_name} gana!"
                self.disable_all_buttons()  # Deshabilitar todos los botones del tablero

            # Cambiar turno automáticamente después de cada adivinanza
            self.selected_guess = None  # Reiniciar la selección
            self.change_turn()

        except ValueError:
            self.result_label.text = "Ingresa un número válido."

    def change_turn(self, *args):
        # Cambiar jugador actual
        self.current_player = 2 if self.current_player == 1 else 1

        # Limpiar campos y preparar para el siguiente jugador
        self.result_label.text = ""

        if self.current_player == 1:
            self.label.text = f"{self.manager.player1_name} adivina."
            self.matrix_layout_player1.opacity = 1
            self.matrix_layout_player1.disabled = False
            self.matrix_layout_player2.opacity = 0
            self.matrix_layout_player2.disabled = True
        else:
            self.label.text = f"{self.manager.player2_name} adivina."
            self.matrix_layout_player1.opacity = 0
            self.matrix_layout_player1.disabled = True
            self.matrix_layout_player2.opacity = 1
            self.matrix_layout_player2.disabled = False

    def disable_all_buttons(self):
        """ Deshabilita todos los botones de ambos tableros """
        for button in self.matrix_buttons_player1 + self.matrix_buttons_player2:
            button.disabled = True

    def quit_game(self, *args):
        """ Salir de la aplicación """
        App.get_running_app().stop()

# Clase principal de la aplicación
class BattleShipApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(Player1HideScreen(name='player1_hide'))
        sm.add_widget(Player2HideScreen(name='player2_hide'))
        sm.add_widget(GuessScreen(name='guess'))
        return sm

if __name__ == '__main__':
    BattleShipApp().run()