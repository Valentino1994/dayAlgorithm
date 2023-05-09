import sys
sys.stdin = open("input.txt")

n = int(input())
a_list = list(map(int, input().split(" ")))
m = int(input())
numbers = list(map(int, input().split(" ")))

for number in numbers:
    if number in a_list:
        print("1")
    else:
        print("0")