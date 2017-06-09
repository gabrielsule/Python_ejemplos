class Auto:
    def __init__(self, **kwargs):
        self._color = kwargs.get('color', 'rojo')

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

def main():
    auto = Auto(color = 'azul')
    print(auto.get_color())

if __name__ == '__main__': main()