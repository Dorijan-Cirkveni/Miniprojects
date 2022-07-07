class Emulator:
    def __init__(self):
        self.data = dict()
        self.current = 0

    def move_right(self):
        self.current += 1
        return

    def move_left(self):
        self.current -= 1
        return

    def change(self, mode, setTo=1):
        k = self.current
        n = self.data.get(k, 0)
        if mode is None:
            n = setTo
        elif mode is True:
            n += setTo
        else:
            n -= setTo
        n %= 256
        if n == 0:
            self.data.pop(k)
        else:
            self.data[k] = n
        return

    def get(self):
        return self.data.get(self.current, 0)

    def print(self, asc2=False):
        cur = self.get()
        if asc2:
            print(cur, end=',')
        else:
            print(chr(cur))

    def input(self, asc2=False):
        cur = input('Input character:')
        if asc2:
            self.change(False, int(cur))
        else:
            self.change(False, ord((cur + '0')[0]))

    def run_simple(self, S):
        for e in S:
            if e == '>':
                self.move_right()
            elif e == '<':
                self.move_left()
            elif e == '-':
                self.change(False)
            elif e == '+':
                self.change(True)
        return

    def get_data(self):
        X = [e for e in self.data.items()]
        X.sort()
        if len(X) == 0:
            return []
        a = X[0][0]
        b = X[-1][0] + 1
        R = [0 for i in range(a, b)]
        for (c, d) in X:
            R[c - a] = d
        return '{}-{}:{}'.format(a, b, R)


def main():
    X = '>--->--->--->+>+++>--->>-->->++>->->+>--->->--->>->+++>+++>-->+>+>--->++>--->->++>-->->--->-->->->-->->-->' \
        '--->->++>->->+>--->->+>+>--->>--->->--->--->->+>+>--->->--->->>-->->++>->->+++>-->->--->>->+>+>--->+>->->+' \
        '++>+++>-->+++>--->->--->++>-->+>+>--->+>+++>--->->-->->-->--->->++>->->+>--->->++>-->->--->-->->+++>+++>--' \
        '>->->->>->-->+>+>--->++>-->->--->-->->+>+>--->+++>+>-->->->-->--->+>-->+>+>--->->--->->++>-->->+++>+++>-->' \
        '+>+>--->+>->-->+++>>-->++>->-->++>->-->+>+>--->+>--->->+++>-->->+>+>--->->>->+>->->>--->->->->->--->-->->+' \
        '>->->++>-->->+++>->-->+>+>--->>--->->+++>--->->+>->->+>+>--->++>--->->++>-->->--->-->->->--->->+++>-->->--' \
        '>--->->>--->->->->->+>+>--->>--->->++>-->->--->-->->++>--->->+++>+++>-->+>-->->>>-->+ '
    Y = '[<+++[-<+++++++>]<+++[-<+++++++>]<+++[.>]<]'
    A = '+>>>+>>++<<<<<--'
    sim = Emulator()
    print(sim.get_data())
    for e in X:
        sim.run_simple(e)
    print(sim.get_data())
    return


if __name__ == "__main__":
    main()
