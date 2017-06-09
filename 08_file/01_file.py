#r = read
#w = write
#a = append
f = open('lines.txt', 'r')

for line in f:
    print(line, end='')