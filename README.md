María Valentina Artola

## Descripción

Este proyecto es una implementación del juego de ajedrez utilizando Python, ejecutable mediante Docker, se han modificado algunas reglas tradicionales del juego, las cuales se describen a continuación.

## Reglas del Juego

El ajedrez es un juego de estrategia para dos jugadores, que se juega sobre un tablero de 8x8 casillas alternas en color blanco y negro. 
Cada jugador controla 16 piezas con el objetivo de capturar todas las piezas del jugador contrario, también pueden terminar la partida si ambos jugadores selecionan la opción de empate (decision que debe ser mutua).

**Movimiento de las Piezas**:
   - **Peón**: Avanza una casilla hacia adelante, pero captura en diagonal. Puede moverse dos casillas hacia adelante en su primer movimiento.
   - **Torre**: Se mueve horizontal o verticalmente cualquier número de casillas.
   - **Caballo**: Se mueve en forma de "L", dos casillas en una dirección y una en perpendicular.
   - **Alfil**: Se mueve diagonalmente cualquier número de casillas.
   - **Dama**: Combina los movimientos de la torre y el alfil.
   - **Rey**: Se mueve una casilla en cualquier dirección.

**Promoción del Peón**: Cuando un peón alcance la última fila, este promocionará a reina.

## Instrucciones para Ejecutar el Juego

Este proyecto está preparado para ejecutarse mediante Docker. A continuación, se detallan los pasos para su correcta ejecución:

### Requisitos Previos

Asegúrate de tener instalado Docker en tu sistema. Puedes consultar la documentación oficial de Docker para su instalación: [Docker Installation Guide](https://docs.docker.com/get-docker/).

### Clonación del Repositorio

Clona el repositorio en tu máquina local usando el siguiente comando:
git clone https://github.com/um-computacion-tm/ajedrez-2024-valeartola.git
cd ajedrez-2024-valeartola

### Para construir la imagen Docker del juego, ejecuta el siguiente comando:
docker buildx build -t ajedrez-2024-valeartola .

### Una vez construida la imagen, puedes ejecutar el juego con el siguiente comando:
docker run -i ajedrez-2024-valeartola


# CircleCI

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-valeartola/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-valeartola/tree/main)
# Codeclimate

[![Maintainability](https://api.codeclimate.com/v1/badges/e6202e3b2212176a6c09/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-valeartola/maintainability)

# Test Codeclimate
<a href="https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-valeartola/test_coverage"><img src="https://api.codeclimate.com/v1/badges/e6202e3b2212176a6c09/test_coverage" /></a> 