class Auto:
    def __init__(self, color = 'rojo'):
        self._color = color

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

def main():
    auto = Auto()
    print(auto.get_color())
    auto.set_color('azul')
    print(auto.get_color())

if __name__ == '__main__': main()