def group_counter(L):
    n=len(L)
    c=0
    used=set()
    for i in range(len(L)):
        cur=i
        if cur in used:
            continue
        while cur not in used:
            used.add(cur)
            cur=L[cur]
        c+=1
    return c


def main():
    print(group_counter([15-i for i in range(16)]))
    return


if __name__ == "__main__":
    main()
