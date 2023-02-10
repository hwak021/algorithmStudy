n = int(input())
num_list = list(map(int, input().split()))
max = -1000000
min = 1000000
for num in num_list:
    if max < num:
        max = num
    if min > num:
        min = num
print(str(min) + " " + str(max))
