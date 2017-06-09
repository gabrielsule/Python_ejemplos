def main():
    test(55, 22, 33, 44)

def test(a, *args):                    #parametro tuple
    print(a)
    for i in args:
        print(i, end=' ')


if __name__ == '__main__': main()