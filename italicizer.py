def italicize(s):
    b = False
    res = ''
    for e in s:
        if e == '"':
            if b:
                res += '{\\i}' + e
            else:
                res += e + '{i}'
            b=not b
        else:
            res += e
    return res


def main():
    F=open('test_in.txt','r')
    X=F.read()
    F.close()
    print(italicize(X))
    return


if __name__ == "__main__":
    main()
