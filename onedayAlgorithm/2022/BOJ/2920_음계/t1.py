import sys
sys.stdin = open("input.txt")

scales = list(map(int, input().split(" ")))

answer = ""
temp = 0
for i in range(len(scales) - 1):
    next_scale = scales[i] - scales[i + 1]
    if i == 0:
        temp = next_scale
    else:
        if temp != next_scale:
            answer = "mixed"
            break

if answer != "mixed":
    if temp == 1:
        answer = "descending"
    else:
        answer = "ascending"

print(answer)
