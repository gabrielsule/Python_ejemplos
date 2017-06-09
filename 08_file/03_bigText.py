#r = read
#w = write
#a = append
buffersize = 50000              #buffer aproximado del file

f_read = open('bigfile.txt', 'r')
f_write = open('new.txt', 'w')

buffer = f_read.read(buffersize)
while len(buffer):
    f_write.write(buffer)
    print('.', end='')          #mostrar avance
    buffer = f_read.read(buffersize)

print()
print('copiado')