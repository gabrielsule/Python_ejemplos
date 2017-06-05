import re

fh = open('raven.txt')
pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
for line in fh:
    if re.search(pattern, line):
        print(line, end='')