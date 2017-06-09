#r = read
#w = write
#a = append
f_read = open('lines.txt', 'r')
f_write = open('new.txt', 'w')

for line in f_read:
    print(line, file = f_write, end='')

print('copiado')