import sys
sys.stdin = open("input.txt", "r")

N = int(input())
commands = list(input().split())

console = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
now = [0, 0]

for command in commands:
    r, c = console[command]
    if N < (now[0] + r) or (now[0] + r) < 0 or N < (now[1] + c) or (now[1]) + c < 0:
        continue
    now[0] += r
    now[1] += c

print(now[0]+1, now[1]+1)