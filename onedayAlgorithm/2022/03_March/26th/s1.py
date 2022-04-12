def solution(logs):
    answer = -1
    log_name = ["team_name", "application_name", "error_level", "message"]
    flag = False
    for log in logs:
        # log가 100이상이면 뺀다.
        if len(log) >= 100:
            answer += 1
            continue

        # " : 를 기준으로 나누고, 다시 빈칸을 기준으로 나누면 형식을 파악할 수 있다."
        # tmp = ['   team_name', 'db  application_name', 'dbtest error_level', 'info message', 'test']
        # log_arr = ['', '', '', 'team_name', 'db', 'application_name', 'dbtest', 'error_level', 'info', 'message', 'test']
        tmp = log.split(" : ")
        log_arr = []
        for t in tmp:
            log_arr += t.split(" ")

        # log_arr을 기준으로 틀린 형식을 잡아낸다.
        name_idx = 0
        # 형식이 올바르다면 인덱스 별로 알맞게 log_name이 들어가 있을 것이다.
        for i in range(0, len(log_arr) - 3, 3):
            if log_arr[i] != log_name[name_idx]:
                answer += 1
                flag = True
                break

            # 다음 형식으로 넘어가면서 계속 파악해준다.
            name_idx += 1

        if flag:
            flag = False
            continue

        # 혹시 누락이 되어 있다면 3까지 오지 못할 것이다.
        if name_idx != 3:
            answer += 1

    return answer

logs = ["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange",
        "no such file or directory",
        "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11",
        "team_name : recommend application_name : recommend error_level : info message : Success!",
        "   team_name : db application_name : dbtest error_level : info message : test",
        "team_name     : db application_name : dbtest error_level : info message : test",
        "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]

print(solution(logs))