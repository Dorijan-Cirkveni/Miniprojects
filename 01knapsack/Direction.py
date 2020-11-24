class Direction:
    def __init__(self, value, previous):
        self.value = value
        self.previous: Direction = previous

    def buildList(self):
        if self.previous is None:
            return list()
        L = self.previous.buildList()
        L.append(self.value)
        return L
