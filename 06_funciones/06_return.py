def main():
    print(test())
    for i in test():
        print(i, end=' ')

def test():
    return range(22)

if __name__ == '__main__': main()