import sys
sys.stdin = open("input.txt")

target = int(input())
ans = abs(100 - target)
n = int(input())
broken_button = set(input().split()) if n != 0 else set()

# 작은수에서 큰수로 이동할땐 500,000 까지만 보면 되지만
# 반대로 큰수에서 작은수로 내려올수도 있으므로 1,000,000 까지 봐야함
for num in range(1000001):
    for N in str(num):
        if N in broken_button:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - target))

print(ans)