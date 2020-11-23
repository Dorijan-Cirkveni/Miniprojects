class KnapsackSparseList:
    def __init__(self):
        self.options:list[tuple] = [(0, (0, None))]
        self.size=1
        return

    def addItem(self, newWeight, newValue):
        newOptions:list[tuple] = [(0, (0, None))]
        j=0
        current=-1
        n=self.size
        for i in range(1,n):
            weight=self.options[j][0]+newWeight
            while weight<self.options[i][0]:
                if newOptions[-1][0]==value:
                    if 
        return
