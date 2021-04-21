class TrustNetworkNode:
    def __init__(self, __id, trusts=None, actionLogs):
        if trusts is None:
            trusts = dict()
        self.__id = __id
        self.trusts = trusts
        self.actionLogs=actionLogs
        return
    def logAction(self,action):
        for e in self.actionLogs:
            e:list
            e.append(action)
        return
    def setTrust(self, node_id, node, trust_level):
        self.logAction((0,node_id,trust_level))
        self.trusts[node_id]=(node,trust_level)
        return
    def verify_ver1(self, ver_id, recursionLimit, default=0, minTrust=0.5):
        self.logAction((1,ver_id))
        if ver_id in self.trusts:
            return ver_id[1]
        elif recursionLimit>0:
            res_sum=0
            res_div=0
            for e in self.trusts.values():
                if e[1]<minTrust:
                    continue
                el:TrustNetworkNode=e[0]
                res_sum+=el.verify_ver1(ver_id,recursionLimit-1)
                res_div+=1
            if res_div!=0:
                res_sum/=res_div
            return res_sum
        else:
            return default



def main():
    return


if __name__ == "__main__":
    main()
