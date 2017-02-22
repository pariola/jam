import string

letters = string.ascii_lowercase
two = letters[:3]
t3 = letters[3:6]
f4 = letters[6:9]
f5 = letters[9:12]
six = letters[12:15]
svn = letters[15:19]
e8 = letters[19:22]
nine = letters[22:]

for case in range(int(input())):
    data = ""
    sentence = input()
    for letter in sentence:
        if letter in two:
            if data[-1:] == str(2):
                data += " "
            for i in range(two.index(letter) + 1):
                data += "2"
        if letter in t3:
            if data[-1:] == str(3):
                data += " "
            for i in range(t3.index(letter) + 1):
                data += "3"
        if letter in f4:
            if data[-1:] == str(4):
                data += " "
            for i in range(f4.index(letter) + 1):
                data += "4"
        if letter in f5:
            if data[-1:] == str(5):
                data += " "
            for i in range(f5.index(letter) + 1):
                data += "5"
        if letter in six:
            if data[-1:] == str(6):
                data += " "
            for i in range(six.index(letter) + 1):
                data += "6"
        if letter in svn:
            if data[-1:] == str(7):
                data += " "
            for i in range(svn.index(letter) + 1):
                data += "7"
        if letter in e8:
            if data[-1:] == str(8):
                data += " "
            for i in range(e8.index(letter) + 1):
                data += "8"
        if letter in nine:
            if data[-1:] == str(9):
                data += " "
            for i in range(nine.index(letter) + 1):
                data += "9"
        if letter == " ":
            if data[-1:] == str(0):
                data += " "
                data += "0"

    print("Case #{}: {}".format(case + 1, data))
