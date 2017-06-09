class Transporte:
    def velocidad(self): print('alguna velocidad')
    def ruedas(self): print('posee ruedas')

class Auto(Transporte):
    def color(self):
        print('rojo')
    def movimiento(self):
        print('acelera')

def main():
    auto = Auto()
    auto.color()
    auto.movimiento()
    auto.velocidad()
    auto.ruedas()

if __name__ == '__main__': main()