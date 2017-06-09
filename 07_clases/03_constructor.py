class Auto:
    def __init__(self, color = 'rojo'):
        self._color = color

def main():
    auto = Auto()
    print(auto._color)
    auto._color = 'blanco'
    print(auto._color)

if __name__ == '__main__': main()