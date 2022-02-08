import sys
sys.stdin = open("input.txt", 'r')
#input = sys.stdin.readline

str1 = input()
str2 = input()

cnt = 0
str1_idx = 0
str2_idx = 0

while str1_idx < len(str1) and str2_idx < len(str2):
    if str1[str1_idx] == str2[str2_idx]:
        cnt += 1
        str2_idx += 1
    else:
        str1_idx += 1

print(cnt)