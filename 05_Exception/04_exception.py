#funcion readline
def readline(filename):
    fh = open(filename)
    return fh.readlines()

try:
    for line in readline('xlines.txt'):
        print(line.strip())
except IOError as e:
    print('no se puede abrir el archivo', e)