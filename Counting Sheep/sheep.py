for case in range(int(input())):

    N = int(input())
    last = 0
    L = set()

    for i in range(1, 1001):
        x = i * N
        if len(L) != 10:
            for a in (str(x)):
                L.add(a)
        if len(L) == 10:
            last = x
            break

    msg = str(last)
    if last == 0:
        msg = "INSOMNIA"

    print("Case #{}: {}".format(case + 1, msg))
