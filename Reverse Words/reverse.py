for case in range(int(input())):
    finalword = ""
    words = list(str(input()).split(" "))
    for word in words:
        finalword = word + " " + finalword
    print("Case #{}: {}".format(case + 1, finalword))
