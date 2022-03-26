def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = []
    remote_workers = [[] for _ in range(num_teams + 1)]
    office = [0] * (num_teams + 1)
    # 재택 근무인지 파악하면서 재택 근무일 경우에는 해당하는 팀 인덱스에 사원번호를 넣어줌.
    for i, employee in enumerate(employees):
        worker_num = i + 1
        arr = employee.split(" ")
        team_num = int(arr[0])

        # 재택 근무인지 파악한다.
        remote = True
        for j in range(1, len(arr)):
            # 보면서 업무가 하나라도 재택이 불가능하면 False로 바꿔주고 office에 해당 팀이 출근한다는 것을 체크해준다.
            if arr[j] in office_tasks:
                remote = False
                office[team_num] = 1
                break

        # 만약 remote work가 가능하다면
        if remote:
            remote_workers[team_num].append(worker_num)

    # office에 출근하는 사람이 없다면 맨 앞 사람을 pop 해준다.
    for i in range(1, len(office)):
        if not office[i]:
            remote_workers[i].pop(0)

    # 재택근무 계산이 끝났음으로 answer에 넣어준다.
    for worker in remote_workers:
        answer.extend(worker)

    return answer