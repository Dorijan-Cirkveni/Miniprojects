from Direction import Direction


class KnapsackSparseList:
    def __init__(self, limit: int):
        self.options: list[tuple] = [(0, 0, None)]
        self.size = 1
        self.limit: int = limit
        return

    def addItem(self, newWeight, newValue):
        newOptions: list[(int, int, Direction)] = []
        j = 0
        current = -1
        n = self.size
        withinLimit = True
        cur_i = self.options[0]
        newOptions.append((cur_i[0], cur_i[1], Direction(False, cur_i[2])))

        for cur_i in self.options[1:]:
            while withinLimit:
                cur_j = self.options[j]
                weight = cur_j[0] + newWeight
                if weight > self.limit:
                    withinLimit = False
                    break
                c = weight - cur_i[0]
                if c > 0:
                    break
                else:
                    newOptions.append((weight, cur_j[1] + newValue, Direction(True, cur_j[2])))
                j += 1
            last_el = newOptions[-1]
            if last_el[0] == cur_i[0]:
                if last_el[1] > cur_i[1]:
                    continue
                else:
                    newOptions.pop()
            newOptions.append((cur_i[0], cur_i[1], Direction(False, cur_i[2])))

        for cur_j in self.options[j:]:
            weight = cur_j[0] + newWeight
            if weight > self.limit:
                break
            newOptions.append((weight, cur_j[1] + newValue, Direction(True, cur_j[2])))

        self.options = newOptions
        self.size = len(newOptions)
        return
