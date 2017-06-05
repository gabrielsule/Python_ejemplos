try:
    fh = open("xlines.txt")             #sacar la x
except:
    print('no se pudo abrir el archivo')
else:
    for line in fh:
        print(line.strip())