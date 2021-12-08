# 로직은 맞았는데 시간초과가 자꾸 난다.
# 나중에 알고리즘을 더 공부하고 다시 풀어보자
def solution(orders, course):
    answer = []

    # 먼저 모든 menu들의 리스트를 만든다.
    tmp_menu_list = []
    for order in orders:
        for menu in order:
            if menu not in tmp_menu_list:
                tmp_menu_list.append(menu)

    # menu들의 조합이 정렬되어서 나와야하기 때문에 미리 정렬을 해둔다.
    menu_list = sorted(tmp_menu_list)
    # 그 후 부분집합을 만든다.
    menu_count_dict = {}
    for i in range(1 << len(menu_list)):
        tmp_course = []
        for j in range(len(menu_list)):
            if i & (1 << j):
                tmp_course.append(menu_list[j])
        # 부분집합의 길이가 course안에 들어 있다면
        if len(tmp_course) in course:
            menu = "".join(tmp_course)
            # 검사를 하고 count를 세서 dict에 넣어준다.
            for order in orders:
                flag = True
                for tmp in tmp_course:
                    if tmp not in order:
                        flag = False
                        break
                if not flag:
                    continue
                if menu not in menu_count_dict:
                    menu_count_dict[menu] = 1
                else:
                    menu_count_dict[menu] += 1

    # 그 후 course의 개수별로 최대값을 파악해서 넣어준다.
    for number in course:
        tmp_list = []
        tmp_max = 0
        for key, value in menu_count_dict.items():
            if value < 2:
                continue
            if len(key) == number:
                if value < tmp_max:
                    continue
                if value == tmp_max:
                    tmp_list.append(key)
                else:
                    tmp_list = []
                    tmp_max = value
                    tmp_list.append(key)

        for item in tmp_list:
            answer.append(item)

    return sorted(answer)

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]

print(solution(orders, course))