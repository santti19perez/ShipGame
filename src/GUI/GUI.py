import sys
sys.path.append("src")
from Logic.NavalWarfare import Player, NavalWarfare
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class NavalWarfareApp(App):
    def build(self):
        # Crear el layout principal
        self.juego = NavalWarfare(Player("Jugador 1"), Player("Jugador 2"))
        main_layout = BoxLayout(orientation='vertical')

        # Crear el layout del tablero
        self.board_layout = GridLayout(cols=5, rows=8)
        self.buttons = []

        for i in range(8):
            row = []
            for j in range(5):
                btn = Button(text=' ')
                btn.bind(on_press=self.button_pressed)
                self.board_layout.add_widget(btn)
                row.append(btn)
            self.buttons.append(row)

        main_layout.add_widget(Label(text='Tablero de Batalla Naval'))
        main_layout.add_widget(self.board_layout)

        # Layout para ingresar coordenadas
        input_layout = BoxLayout(orientation='horizontal')
        self.position_input = TextInput(hint_text='Ej: A1', multiline=False)
        input_layout.add_widget(self.position_input)

        self.place_ship_button = Button(text='Posicionar Barco')
        self.place_ship_button.bind(on_press=self.place_ship)
        input_layout.add_widget(self.place_ship_button)

        main_layout.add_widget(input_layout)

        return main_layout

    def button_pressed(self, instance):
        # Obtener la posición del botón presionado
        for i, row in enumerate(self.buttons):
            for j, btn in enumerate(row):
                if btn == instance:
                    print(f"Botón en posición {i}, {j} presionado")
                    # Aquí puedes llamar a la función shoot con la posición correspondiente
                    break

    def place_ship(self, instance):
        position = self.position_input.text
        if position:
            try:
                self.juego.posicionate_ship(position)
                # Actualiza la interfaz para reflejar el cambio en el tablero
                letra, fila = self.juego.convert_location(position)
                self.buttons[fila][letra].text = 'S'  # Marca 'S' para barco
                self.position_input.text = ''
            except ValueError as e:
                print(e)

if __name__ == '__main__':
    NavalWarfareApp().run()
