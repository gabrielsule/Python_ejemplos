def main():
    for i in inclusive_test(5, 22, 4):        #start, stop, step
        print(i, end=' ')


def inclusive_test(*args):
    numargs = len(args)
    if numargs < 1:
        raise TypeError('requiere por lo menos un argumento')
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError('son solo 3 argumentos, paso {} argumentos'.format(numargs))

    n = start
    while n <= stop:
        yield n
        n += step


if __name__ == '__main__': main()