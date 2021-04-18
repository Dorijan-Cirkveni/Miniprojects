import random

from typing import List


class ConnectionNetwork:
    def __init__(self, memberCount, connectionOdds=0.001, loadFile=''):
        self.memberCount = memberCount
        if memberCount > 10 ** 6:
            raise Exception("MEMBER COUNT TOO BIG.")
        L = [set() for i in range(memberCount)]
        for i in range(memberCount):
            for j in range(i + 1, memberCount):
                if random.random() < connectionOdds:
                    L[i].add(j)
                    L[j].add(i)
        self.connections: List[set] = L
        return

    def CountGroups(self):
        count = 0
        current = 0
        used = set()
        for current in range(self.memberCount):
            if current in used:
                used.remove(current)
                continue
            acc = {current}
            new = {current}
            while len(new) != 0:
                newnew = set()
                for e in new:
                    for f in self.connections[e]:
                        f: int
                        if f < current or f in acc:
                            continue
                        newnew.add(f)
                acc |= newnew
                new = newnew
            used |= acc
            count += 1
        return count

    def RunReferralScheme(self, founderCount):
        inactive = set()
        active = set(random.sample(range(1,self.memberCount), founderCount))
        referrals = {e: None for e in active}
        count = founderCount
        log = [count]
        while len(active) != 0:
            tmp = set()
            for e in active:
                for f in self.connections[e]:
                    if f not in active and f not in inactive:
                        tmp.add(f)
                        referrals[f] = e
                tmp.add(e)
            inactive |= active
            active = tmp
            log.append(len(tmp))
        return log, referrals


def main():
    cn = ConnectionNetwork(10000)
    _ = input("Run referral scheme")
    log, referrals = cn.RunReferralScheme(1)
    print(log, len(referrals))
    return


if __name__ == "__main__":
    main()
