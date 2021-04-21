from typing import List


def line(x):
    return (7 & (x << 1)) ^ (x >> 1) ^ x


class Breakout:
    def __init__(self, size):
        self.size = size
        return

    def check(self, buttons: List[int]):
        if self.size == 1:
            return buttons[0][0]
        res = list()
        last = 0
        for i in range(self.size - 1):
            thisline = line(buttons[i])
            thisline ^= last ^ buttons[i + 1]
            res.append(thisline)
            last = buttons[i]
        thisline = line(buttons[-1]) ^ last
        res.append(thisline)
        return res

    def checkFirst(self, firstLine: int):
        FULL = (1 << self.size) - 1
        res = [firstLine]
        lightsLine = line(firstLine)
        for i in range(self.size):
            current = FULL ^ lightsLine
            lightsLine = line(current) ^ firstLine
            firstLine = current
            res.append(firstLine)
        return res, firstLine


def main():
    X = Breakout(3)
    for i in range(8):
        K = X.checkFirst(i)
        print(K, X.check(K[0]))
    return


if __name__ == "__main__":
    main()
