# NAVAL WARFAME GAME

Este proyecto es un sistema de batallas navales multijugador con manejo de jugadores, tableros y lógica de juego. La aplicación permite crear jugadores, iniciar juegos entre ellos y realizar las acciones típicas del juego de batallas navales, como posicionar barcos y disparar a las posiciones del tablero enemigo.

## Requisitos
Python 3.6 o superior, en este casp nososotros usamos anancoda
PostgreSQL (para gestionar la base de datos)

## Estructura del proyecto


│
├── src/
│   ├── controller/
│   │   └── game_controller.py         # Controlador principal del juego
│   ├── model/
│   │   ├── player_model.py             # Modelo de Jugador
│   │   └── naval_warfare.py       # Lógica principal del juego
│   ├── db_connection.py           # Conexión con la base de datos
│   └── config.py                  # Archivo de configuración de la base de datos
│
├── test/
│   └── test_player.py            # Pruebas unitarias para el modelo Jugador
│
└── README.md        

## Instalación de dependencias
Instalar las librerías necesarias:

                               pip install psycopg2


## Base de datos
El proyecto utiliza PostgreSQL como base de datos. El esquema de la base de datos incluye las siguientes tablas:

jugadores: Almacena la información básica de los jugadores.
juegos: Gestiona las partidas entre dos jugadores.
tableros: Representa el estado de cada tablero de un jugador en un juego.

## Controlador del juego
El archivo controlador.py maneja las interacciones principales con los jugadores y la lógica de juego.

Funciones principales:

Crear jugador: Añade un nuevo jugador a la base de datos.
Actualizar jugador: Modifica el nombre de un jugador existente.
Eliminar jugador: Borra un jugador de la base de datos.
Iniciar juego: Inicia un juego entre dos jugadores.
Colocar barco: Posiciona un barco en el tablero de un jugador.
Realizar disparo: Ataca una posición del tablero del oponente.
Verificar fin del juego: Comprueba si el juego ha terminado.
Obtener ganador: Devuelve el jugador que ganó la partida.

## Ejecución
Iniciar el juego:
Ejecuta el archivo main.py para comenzar el programa de consola:

                                        python src/main.py
El menú principal ofrece las siguientes opciones:

Crear jugador
Ver jugadores
Actualizar jugador
Eliminar jugador
Iniciar juego
Salir

## Pruebas
El proyecto incluye un conjunto de pruebas unitarias para verificar la funcionalidad del modelo de jugadores.

Para ejecutar las pruebas, corre el siguiente comando:

                                     python -test/ test_player.py

