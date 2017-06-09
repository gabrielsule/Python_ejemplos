buffersize = 50000              #buffer aproximado del file

f_read = open('olives.jpg', 'rb')
f_write = open('new.jpg', 'wb')

buffer = f_read.read(buffersize)
while len(buffer):
    f_write.write(buffer)
    print('.', end='')          #mostrar avance
    buffer = f_read.read(buffersize)

print()
print('copiado')