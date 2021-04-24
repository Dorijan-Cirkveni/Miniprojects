from collections import deque

from typing import List


def createTree(s, up='({[', down=')}]', same=';'):
    res = ['']
    log = [res]
    quoted = None
    for e in s:
        cur: List[(list, str)] = log[-1]
        if quoted is not None:
            cur[-1] += e
            if e == quoted:
                cur.append('')
                quoted = None
            continue
        if e in "\"\'":
            quoted = e
            cur[-1] += e
            continue
        if e in up:
            cur.append(e)
            new = ['']
            cur.append(new)
            log.append(new)
            continue
        if e in down:
            _ = log.pop()
            cur = log[-1]
            cur.append(e)
            cur.append('')
            continue
        if e in same:
            cur.append(e)
            cur.append('')
            continue
        cur[-1] += e
    return res


def justify(L, space, itemSurplus=1):
    if len(L) == 0:
        return None
    if not L[0]:
        return None
    L2 = [L[0]]
    c = 0
    for e in L[1:]:
        d = len(e) - itemSurplus
        c += d
        if c > space:
            L2.append(e)
            c = d
            continue
        L2[-1] += e
    return L2


def merge(T, mergeLimit=60, itemSurplus=1):
    c = 0
    NT = []
    cur_L = []
    T.append([])
    for i in range(len(T)):
        el = T[i]
        if type(el) != str:
            el = merge(el, mergeLimit, itemSurplus)
            if type(el) != str:
                ext = justify(cur_L, mergeLimit, itemSurplus)
                if ext is not None:
                    NT.extend(ext)
                NT.append(el)
            if len(el)!=0 and not el[0]:
                print(el)
        cur_L.append(el)
    if len(NT) == 1:
        return NT[0]
    return NT


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
        T2 = merge(T)
        if type(T2) != str:
            generateString(T, L2)
            continue
        L2.append(T2)
    print('Done!')
    F = open(outputPath, 'w')
    F.write('\n'.join(L2))
    F.close()
    return


def test():
    beautifyFile('beautifier\\test_in.txt', 'beautifier\\test_out.txt')
    return


def main():
    data = 'beautifier\\test_in.txt', 'beautifier\\test_out.txt'
    # input('Input and output files, separated by comma:').split(',')
    ins = data[0]
    outs = data[1]
    beautifyFile(ins, outs)
    return


if __name__ == "__main__":
    main()
