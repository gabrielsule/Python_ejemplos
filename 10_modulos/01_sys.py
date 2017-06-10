import sys
import os
import urllib.request
import random
import datetime

#sys
print('Python version {}.{}.{}'.format(*sys.version_info))
print(sys.platform)

#OS
print(os.name)
print(os.getenv('PATH'))

#url
page = urllib.request.urlopen('https://www.skytorrents.in/')
print(page)
for line in page:
    print(str(line, encoding='utf_8'), end='')

#random
print(random.randint(1,25))
x = list(range(25))
print(x)
random.shuffle(x)
print(x)

#datetime
now = datetime.datetime.now()
print(now)
print(now.year, now.month, now.day, now.hour, now.second, now.microsecond)