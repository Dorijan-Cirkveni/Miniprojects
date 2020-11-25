from KnapsackSparseList import KnapsackSparseList


def main():
    X = KnapsackSparseList(4)
    for e in [(2, 1), (2, 2), (3, 100)]:
        X.addItem(e[0], e[1])
        print([(e[0],e[1],None if e[2] is None else e[2].value) for e in X.options])
    return


if __name__ == "__main__":
    main()
