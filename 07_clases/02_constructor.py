class Auto:
    def __init__(self, value):
        self._v = value
    def color(self):
        print('rojo')
    def movimiento(self):
        print('acelera')
    def patente(self):
        print(self._v)

def main():
    auto = Auto('abc123')
    auto.color()
    auto.movimiento()
    auto.patente()

if __name__ == '__main__': main()