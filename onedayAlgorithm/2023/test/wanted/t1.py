import sys
sys.stdin = open("input1.txt")

N = int(input())
states = list(map(int, input().split(" ")))

prefix_sum = []
answer = 0
for i in range(1, N+1):
    temp_states = states[:i]
    left_count = temp_states.count(1)
    right_count = temp_states.count(2)
    prefix_sum.append((left_count, right_count))
    answer = max(abs(left_count - right_count), answer)


