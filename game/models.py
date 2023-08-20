"""S C R A B B L E
2-4 jugadores

CLASES¿¿¿

- tablero
    -casilla
        - multiplicadores
- comodin
- jugador
    -puntaje
- bolsa
    - letras: valor letra, valor ptos
-game
    -turnos

-----------------------------------------------------------------

- cobertura: que los test cubran el 90% de los casos posibles (usar CodeClimate o coveralls.io)
- en cada commit todos los test deben estar funcionales


#hacer main (probablemente?)
# jugador <--> linea de comandos <--> game


OBJ: repo con integracion continua, coverage, etc. Configurar las cosas"""

import random

class Tile:
    def __init__(self,letter,value):
        self.letter = letter
        self.value = value

class BagTiles:
    def __init__(self):
        self.tiles = [
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
        ]
        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles

    def put(self,tiles):
        self.tiles.extend(tiles)













