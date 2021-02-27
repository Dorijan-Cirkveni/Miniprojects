class NFA:
    def __init__(self, states: list, final: set, transitions):
        self.states: list = states
        self.final: set = final
        for X in transitions:
            if "" not in X:
                X[""] = {}
        self.transitions: list[dict] = transitions  # Example: [{"A"}{1}]
        return

    def process(self, states: set, step):
        newstates = set()
        for e in states:
            T = self.transitions[e]
            if step in T:
                newstates.add(T[step])
            else:
                newstates.add(T[""])
        return newstates


class Checker:
    def __init__(self, keyword: str):
        n = len(keyword)
        X = [i for i in range(n + 1)]
        s = keyword[0]
        L = [{"": {0}} for i in range(n)]
        for i in range(n):
            e = keyword[i]
            L[i][e] = {i + 1}
        for e in L[0]:
            L[0][e].add(0)
        self.nfa = NFA(X, {n}, L)
        self.n = n
        return

    def GenerateIndices(self, string):
        indices = []
        states = {0}
        for i in range(len(string)):
            c = string[i]
            states = self.nfa.process(states, c)
            if self.n in states:
                indices.append(i)
        return indices


class Replacer:
    def __init__(self, k1, k2):
        self.c1: Checker = Checker(k1)
        self.c2: Checker = Checker(k2)
        '''
        self.ind = []
        diff = self.c1.n - self.c2.n
        if diff == 0:
            if k1 == k2:
                self.ind = [0]
        elif diff > 0:
            self.ind = self.c1.GenerateIndices(k2)
        else:
            self.ind = self.c2.GenerateIndices(k1)
        self.diff = diff
        '''
        return

    def Replace(self, start, preserveEndPhrases=False):  # banana, a->na
        A = self.c1.GenerateIndices(start)
        B = self.c2.GenerateIndices(start)
        la = len(A)
        lb = len(B)
        n1 = self.c1.n
        n2 = self.c2.n
        j = 0
        for i in range(0, la):
            a1 = A[i] - n2
            a2 = A[i] + n1
            for j in range(j, lb):
                if B[j] > a1:
                    break
            j0 = j

        # TODO complete this
        return


def main():
    X = [
        ["alphabet", "alpha", "A"]
    ]
    for e in X:
        print(e[0].replace(e[1], e[2]))
        C = Checker(e[1])
    return


if __name__ == "__main__":
    main()
