import re

fh = open('raven.txt')

for line in fh:
    match = re.search('(Len|Neverm)ore', line)
    if match:
        print(line.replace(match.group(), '###'), end='')