class Auto:
    def __init__(self, **kwargs):
        self.variables = kwargs

    def set_varible(self, k, v):
        self.variables[k] = v

    def get_variable(self, k):
        return self.variables.get(k, None)


def main():
    auto = Auto(color = 'rojo')
    #auto = Auto(modelo = '308')

    print(auto.get_variable('color'))
    print(auto.get_variable('modelo'))


if __name__ == '__main__': main()