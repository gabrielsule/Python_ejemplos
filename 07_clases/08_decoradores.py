class Auto:
    def __init__(self):
        self._color = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, c):
        self._color = c

def main():
    auto = Auto()
    auto.color = 'rojo'
    print(auto.color)

if __name__ == '__main__': main()