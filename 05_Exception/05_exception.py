#funcion readline
def readline(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else:
        raise ValueError('debe ser un TXT')

try:
    for line in readline('lines.doc'):
        print(line.strip())
except IOError as e:
    print('no se puede abrir el archivo', e)

except ValueError as e:
    print(e)