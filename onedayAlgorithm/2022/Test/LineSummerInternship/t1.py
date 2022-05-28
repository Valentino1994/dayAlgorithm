def solution(logs):
    answer = []
    # If there is only one log. This is only one well-known problem
    if len(logs) == 1:
        answer.append(logs[0].split(" ")[1])
        return answer

    # To get the amount of users
    users = []
    solvedPersons = dict()
    for log in logs:
        user, problem = log.split(" ")

        if user not in users:
            users.append(user)

        if problem not in solvedPersons:
            solvedPersons[problem] = [user]
        else:
            if user not in solvedPersons[problem]:
                solvedPersons[problem].append(user)

    # cuz there is a case that amount of users is a odd number, I used a double
    halfOfUser = len(users) / 2
    for key, value in solvedPersons.items():

        if len(value) >= halfOfUser:
            answer.append(key)

    return sorted(answer)


logs = ["morgan string_compare", "felix string_compare", "morgan reverse", "rohan sort", "andy reverse", "morgan sqrt"]
# logs = ["kate sqrt"]
print(solution(logs))