N = 10

nums = [1]
factors = [2, 3, 5]
dp = [1]

while len(dp) < N:

    v = nums.pop()
    for factor in factors:
        if v * factor not in dp:
            dp.append(v * factor)
            nums.append(v * factor)

print(dp)