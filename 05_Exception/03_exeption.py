try:
    fh = open("lines.txt")             #sacar la x
    for line in fh:
        print(line.strip())
except IOError as e:
    print('no se pudo abrir el archivo', e)
