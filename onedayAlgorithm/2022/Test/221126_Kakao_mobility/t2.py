def solution(id_list, k):
    answer = 0
    coupon_dict = dict()

    for today, ids in enumerate(id_list):
        users = ids.split(" ")
        for user in users:
            if user in coupon_dict:
                if today not in coupon_dict[user] and len(coupon_dict[user]) < k:
                    coupon_dict[user].append(today)
            else:
                coupon_dict[user] = [today]

    for value in coupon_dict.values():
        answer += len(value)

    return answer

id_list = ["A B C D", "A D", "A B D", "B D"]
k = 2

print(solution(id_list, k))