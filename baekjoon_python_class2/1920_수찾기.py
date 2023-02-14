import sys
N = int(sys.stdin.readline())
num_list1 = list(map(int, sys.stdin.readline().split(' ')))
M = int(sys.stdin.readline())
num_list2 = list(map(int, sys.stdin.readline().split()))
num_list1.sort()

for num in num_list2:
    start, end = 0, N - 1
    check = False
    while start <= end:
        mid = (start + end) // 2
        if num == num_list1[mid]:
            check = True
            break
        elif num > num_list1[mid]:
            start = mid + 1
        else:
            end = mid - 1
    if check:
        print(1)
    else:
        print(0)
