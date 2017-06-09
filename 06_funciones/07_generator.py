def main():
    for i in inclusive_test(0, 22, 1):
        print(i, end=' ')

def inclusive_test(start, stop, step):
    n = start
    while n <= stop:
        yield n
        n += step
        
if __name__ == '__main__': main()