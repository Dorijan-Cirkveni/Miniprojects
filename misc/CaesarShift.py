def CharRotate(c, k=1):
    isLower = c.lower() == c
    num = ord(c.upper()) - ord('A')
    if num not in range(0,26):
        return c
    newnum = (num + k) % 26
    cnew = chr(ord('A') + newnum)
    if isLower:
        cnew = cnew.lower()
    return cnew


def StringRotate(s, k=1):
    return ''.join([CharRotate(e,k) for e in s])

def TestAll(s):
    for i in range(1,26):
        input(str(i)+'\t'+StringRotate(s,i))


def main():
    print(StringRotate('Well that was a nice coding exercise to start the day with.',42))
    return


if __name__ == "__main__":
    main()
