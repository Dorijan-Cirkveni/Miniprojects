class NFA:
    def __init__(self, states: list, final: set, transitions):
        self.states: list = states
        self.final: set = final
        for X in transitions:
            if "" not in X:
                X[""] = {0}
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
        return
    def GenerateIndices(self,string):
        

def main():
    X = [
        ["alphabet", "alpha", "A"]
    ]
    for e in X:
        print(e[0].replace(e[1], e[2]))
        C=Checker(e[1])
    return


if __name__ == "__main__":
    main()
