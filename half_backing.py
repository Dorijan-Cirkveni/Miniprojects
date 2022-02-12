def back_step(value, price1, price2, ratio):
    a = b = value / 2
    b *= price2 / price1
    nv = a + b
    nr = (price2 - price1) / ratio
    return nv, nr


def mul_steps(value, prices, ratio, debug=False):
    X = prices[::-1]
    cur = X.pop()
    nr = cur
    while len(X) > 0:
        las = cur
        cur = X.pop()
        nv, nr = back_step(value, las, cur, ratio)
        if debug:
            print(nv, nr)

        value = nv
    return value, nr


def main():
    for i in range(0, 210, 10):
        for j in range(1,11,1):
            L=[100+(i-100)*k/j for k in range(0,j+1,1)]
            a, b = mul_steps(100, L, 10)
            print('{0:.5}'.format(a), end=',')
        print()
    return


if __name__ == "__main__":
    main()
