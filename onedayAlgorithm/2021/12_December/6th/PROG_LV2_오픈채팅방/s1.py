def solution(record):
    answer = []
    record_list = []
    nickname_dict = {}
    for info in record:
        tmp_list = list(info.split(" "))
        if tmp_list[0] == "Leave":
            record_list.append("{}님이 나갔습니다.".format(tmp_list[1]))

        elif tmp_list[0] == "Change":
            nickname_dict[tmp_list[1]] = tmp_list[2]

        elif tmp_list[0] == "Enter":
            record_list.append("{}님이 들어왔습니다.".format(tmp_list[1]))
            if not nickname_dict:
                nickname_dict[tmp_list[1]] = tmp_list[2]
            else:
                nickname_dict[tmp_list[1]] = tmp_list[2]

    for rec in record_list:
        tmp = rec.split("님")
        answer.append("{}님{}".format(nickname_dict[tmp[0]], tmp[1]))

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))