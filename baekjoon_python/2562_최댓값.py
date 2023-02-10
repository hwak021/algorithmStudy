idx = 0
max = 0
for i in range(1, 10):
    num = int(input())
    if num > max:
        max = num
        idx = i
print(max)
print(idx)