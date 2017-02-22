for case in range(int(input())):
    C = int(input())
    I = int(input())
    P = list(input().split(" "))
    L = set()

    for i in range(len(P)):
        d = P[i]
        P.remove(P[i])
        for j in range(len(P)):
            if (int(d) + int(P[j])) == C:
                L.add((i + 1, j + 2))
        P.insert(i, d)

    x = min(L)

    print("Case #{}: {}".format(case + 1, str(x[0]) + " " + str(x[1])))
