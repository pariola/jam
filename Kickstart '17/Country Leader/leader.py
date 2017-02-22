import string

letters = list(string.ascii_uppercase)

for case in range(int(input())):

    names = []
    counts = []
    fcount = 0

    for a in range(int(input())):
        names.append(str(input()))
    for name in names:
        count = 0
        for letter in letters:
            if name.__contains__(letter):
                name.replace(letter, "")
                count += 1
        if fcount != count: fcount = max(fcount, count)

    names.sort()

    v = ""

    for name in names:
        count = 0
        for letter in letters:
            if name.__contains__(letter):
                name.replace(letter, "")
                count += 1
        if count == fcount:
            v = name
            break

    print("Case #{}: {}".format((case + 1), v))
