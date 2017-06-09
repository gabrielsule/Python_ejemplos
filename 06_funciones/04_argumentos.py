def main():
    test(a = 55, b = 22, c = 33)

def test(**kwargs):
    print(kwargs['b'])
    for k in kwargs:
        print(k, kwargs[k])

if __name__ == '__main__': main()