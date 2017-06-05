try:
    fh = open("xlines.txt")             #sacar la x
except IOError as e:
    print('no se pudo abrir el archivo', e)
else:
    for line in fh:
        print(line.strip())