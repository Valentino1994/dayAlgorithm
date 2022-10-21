def checkWords(words):
    for word in words:
        my_strings = []
        for i in range(len(word)):
            if word[i] in my_strings:
                return False
            else:
                my_strings.append(word[i])

    return True

def solution(S, C):
    # write your code in Python 3.8.10
    if checkWords(S.split(" ")):
        return 0

    for i in range(len(C)):
        temp = 0
        for j in range(len(S)):

            if S[j] == "$":
                continue

            else:
                if temp == C[i]:
                    S = S[:j] + "$" + S[j:]
                    break
                else:
                    temp += 1

        words = S.split("$")

        if checkWords(words):
            return i+1

    return -1

S = 'aabcddcb'
C = [3, 5, 1, 4, 7]
S1 = 'abcd'
C1 = [1, 2]
print(solution(S, C))
print(solution(S1, C1))