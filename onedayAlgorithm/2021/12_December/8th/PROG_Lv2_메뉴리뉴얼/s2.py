def dict_update(d, key):
    if key in d:
        d[key] += 1
    else:
        d[key] = 1

def order_update_rec(d, s, i, rst):
    if i == len(s):
        dict_update(d, rst)
    else:
        order_update_rec(d, s, i+1, rst)
        order_update_rec(d, s, i+1, rst+s[i])

def solution(orders, course):
    order_dict = {}
    for order_i in range(len(orders)):
        orders[order_i] = sorted(orders[order_i])
        order_update_rec(order_dict, orders[order_i], 0, "")

    result = []
    max_v = [ 0 for _ in range(len(course)) ]
    max_key = [ [] for _ in range(len(course)) ]
    for key in order_dict:
        for course_i, course_n in enumerate(course):
            if len(key) == course_n:
                if order_dict[key] > max_v[course_i]:
                    max_v[course_i] = order_dict[key]
                    max_key[course_i] = [key]
                elif order_dict[key] == max_v[course_i]:
                    max_key[course_i].append(key)
    for i, v in enumerate(max_v):
        if v >= 2:
            result += max_key[i]

    return sorted(result)