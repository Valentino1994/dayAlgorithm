import sys
sys.stdin = open("input.txt", "r")
#input = sys.stdin.readline
string = input()

stack = []
number = ''
for s in string:
    if not s.isnumeric():
        stack.append(int(number))
        stack.append(s)
        number = ''
        continue
    number = number + s
stack.append(int(number))

tmp = []
idx = 0
while idx < len(stack):

    if stack[idx] == "+":
        a = tmp.pop()
        b = stack[idx+1]
        tmp.append(a+b)
        idx += 2

    else:
        tmp.append(stack[idx])
        idx += 1

for i in range(len(tmp)-1):
    if tmp[i] == '-':
        tmp[0] -= tmp[i+1]

print(tmp[0])