def solution(s):
    answer = 0

    idx = 0
    tmp = ""
    while idx < len(s):

        if s[idx].isnumeric():
            tmp += s[idx]
            idx += 1
            continue

        if s[idx] == "z":
            tmp += "0"
            idx += 4

        elif s[idx] == "o":
            tmp += "1"
            idx += 3

        elif s[idx] == "t":
            if s[idx + 1] == "w":
                tmp += "2"
                idx += 3
            else:
                tmp += "3"
                idx += 5

        elif s[idx] == "f":
            if s[idx + 1] == "o":
                tmp += "4"
                idx += 4
            else:
                tmp += "5"
                idx += 4

        elif s[idx] == "s":
            if s[idx + 1] == "i":
                tmp += "6"
                idx += 3
            else:
                tmp += "7"
                idx += 5

        elif s[idx] == "e":
            tmp += "8"
            idx += 5

        elif s[idx] == "n":
            tmp += "9"
            idx += 4

    answer = int(tmp)

    return answer

s = "one4seveneighteight"
print(solution(s))