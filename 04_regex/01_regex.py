import re

fh = open('raven.txt')
for line in fh:
    if re.search('(Len|Neverm)ore', line):  #Lenore or Nevermore
        print(line, end='')