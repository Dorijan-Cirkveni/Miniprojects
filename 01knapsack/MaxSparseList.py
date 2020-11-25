class MaxSparseList:
    def __init__(self, firstMember, limit: int,
                 weight: callable = lambda x: x[0],
                 value: callable = lambda x: x[1]):
        self.weight = weight
        self.value = value
        self.data = [firstMember]
        self.limit = limit
        return

    def append(self, newMember):
        w = self.weight(newMember)
        if w > self.limit:
            return 1
        if self.value(self.data[-1]) >= self.value(newMember):
            return 2
        if self.weight(self.data[-1]) == w:
            _ = self.data.pop()
        self.data.append(newMember)
        return 0
