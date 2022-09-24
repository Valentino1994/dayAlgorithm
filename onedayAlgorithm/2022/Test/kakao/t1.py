from collections import defaultdict

def solution(today, terms, privacies):
    answer = []

    termDict = defaultdict()
    todayArr = today.split(".")
    todayInt = (((int(todayArr[0]) * 12) + int(todayArr[1])) * 28) + int(todayArr[2])

    for term in terms:
        temp = term.split(" ")
        termDict[temp[0]] = int(temp[1])

    for i in range(len(privacies)):
        privacy = privacies[i]

        temp = privacy.split(" ")
        year, month, day = temp[0].split(".")
        finishDayInt = (((int(year) * 12) + int(month)) * 28) + int(day) + (28 * termDict[temp[1]])

        if finishDayInt <= todayInt:
            answer.append(i+1)

    return answer

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

today1 = "2020.01.01"
terms1 = ["Z 3", "D 5"]
privacies1 = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
print(solution(today, terms, privacies))
print(solution(today1, terms1, privacies1))