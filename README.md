#NAVAL WARFAME GAME

Este proyecto es un sistema de batallas navales multijugador con manejo de jugadores, tableros y lógica de juego. La aplicación permite crear jugadores, iniciar juegos entre ellos y realizar las acciones típicas del juego de batallas navales, como posicionar barcos y disparar a las posiciones del tablero enemigo.

#Requisitos
Python 3.6 o superior
PostgreSQL (para gestionar la base de datos)

#Estructura del proyecto
bash
Copiar código
naval_warfare_game/

│
├── src/
│   ├── controller/
│   │   └── controlador.py         # Controlador principal del juego
│   ├── model/
│   │   ├── jugador.py             # Modelo de Jugador
│   │   └── naval_warfare.py       # Lógica principal del juego
│   ├── db_connection.py           # Conexión con la base de datos
│   └── config.py                  # Archivo de configuración de la base de datos
│
├── test/
│   └── test_jugador.py            # Pruebas unitarias para el modelo Jugador
│
└── README.md        

#Instalación de dependencias
Instalar las librerías necesarias:

                                                   pip install -r requirements.txt

