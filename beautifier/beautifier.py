from collections import deque

from typing import List


def createTree(s, up='({[', down=')}]', same=';'):
    res = ['']
    log = [res]
    for e in s:
        cur: List[(list, str)] = log[-1]
        if e in up:
            cur.append(e)
            new = ['']
            cur.append(new)
            log.append(new)
        elif e in down:
            _ = log.pop()
            cur = log[-1]
            cur.append(e)
            cur.append('')
        elif e in same:
            cur.append(e)
            cur.append('')
        else:
            cur[-1] += e
    return res


def merge(T, mergeLimit=60, itemSurplus=1):
    c = 0
    for i in range(len(T)):
        el = T[i]
        if type(el) != str:
            el = merge(el, mergeLimit, itemSurplus)
            if type(el) != str:
                return T
            T[i] = el
        c += len(el) - itemSurplus
    if c >= mergeLimit:
        return T
    s = ''.join(T)
    return s


def generateString(T, L: list, indent='-|', depth=0):
    for e in T:
        if type(e) == str:
            L.append(indent * depth + e)
            continue
        generateString(e, L, indent, depth + 1)
    return


def unbeautify(s):
    for e in '\n\t ':
        s = s.replace(e, '')
    return s


def beautifyFile(inputPath, outputPath):
    F = open(inputPath, 'r')
    L = F.read().split("\n")
    F.close()
    L2 = list()
    for e in L:
        T = createTree(e)
        T2 = merge(T, 20)
        if type(T2) != str:
            generateString(T, L2)
            continue
        L2.append(T2)
    F = open(outputPath, 'w')
    F.write('\n'.join(L2))
    F.close()
    return


def test():
    beautifyFile('beautifier\\test_in.txt', 'beautifier\\test_out.txt')
    return


def main():
    ins = input('Input file path:')
    outs = input('Output file path:')
    beautifyFile(ins, outs)
    return


if __name__ == "__main__":
    main()
