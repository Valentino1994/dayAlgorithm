def solution(s, times):
    answer = []
    year, month, day, hour, minute, second = list(map(int, s.split(":")))
    c_year, c_month, c_day, c_hour, c_minute, c_second = list(map(int, s.split(":")))

    is_1day_1saving = 1
    for time in times:
        now_day, now_hour, now_minute, now_second = list(map(int, time.split(":")))
        calculated_time = calculate_times([c_year, c_month, c_day + now_day, c_hour + now_hour, c_minute + now_minute, c_second + now_second])
        # 이미 불가능으로 판별되었다면 돌릴 필요가 없음
        if is_1day_1saving:
            # 연, 월, 일만 필요함
            is_okay = check_1day_1saving([c_year, c_month, c_day], calculated_time[:3])
            is_1day_1saving = is_okay

        c_year, c_month, c_day, c_hour, c_minute, c_second = calculated_time

    answer.append(is_1day_1saving)
    answer.append(check_days([year, month, day], [c_year, c_month, c_day]) + 1)

    return answer

# 일년이 360일, 한달이 30일로 고정여서 datetime을 쓸 수 없음
def calculate_times(now_times):
    year, month, day, hour, minute, second = now_times
    now_sec = (year * (360 * 24 * 60 * 60)) + (month * (30 * 24 * 60 * 60)) + (day * (24 * 60 * 60)) + (hour * (60 * 60)) + (minute * 60) + second

    now_year = now_sec // (360 * 24 * 60 * 60)
    now_sec %= (360 * 24 * 60 * 60)

    now_month = now_sec // (30 * 24 * 60 * 60)
    now_sec %= (30 * 24 * 60 * 60)

    now_day = now_sec // (24 * 60 * 60)
    now_sec %= (24 * 60 * 60)

    now_hour = now_sec // (60 * 60)
    now_sec %= (60 * 60)

    now_minute = now_sec // 60
    now_sec %= 60

    return [now_year, now_month, now_day, now_hour, now_minute, now_sec]

def check_1day_1saving(before, now):
    b_year, b_month, b_day = before
    n_year, n_month, n_day = now
    # 1일 1저축이 실패한 경우의 수
    if n_year - b_year != 0 or n_month - b_month != 0 or n_day - b_day > 1:
        return 0

    return 1

def check_days(before, now):
    b_year, b_month, b_day = before
    n_year, n_month, n_day = now

    result = 0
    result += (n_year - b_year) * 360
    result += (n_month - b_month) * 30
    result += (n_day - b_day)

    return result

s = "2021:04:12:16:08:35"
times = ["01:06:30:00", "01:01:12:00", "00:00:09:25"]

s1 = "2021:04:12:16:08:35"
times1 = ["01:06:30:00", "01:04:12:00"]
print(solution(s, times))
print(solution(s1, times1))