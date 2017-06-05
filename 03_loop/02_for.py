s = 'lorem'

#for basico
for data in s:
    print(data)

# for con break
for data in s:
    if data == 'e':break
    print(data)

#for con indice
for i, data in enumerate(s):
    print(i, data)

#for con indice
for i, data in enumerate(s):
    if data == 'r': print('indice {} de r'.format(i))

#for con archivo
fh = open('lines.txt')
for line in fh.readlines():
    print(line, end='')

