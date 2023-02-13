import sys

n  = int(sys.stdin.readline())
num_list = []
for i in range(n):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()

for num in num_list:
    print(num)

# for i in range(n-1):
#     min = num_list[i]
#     idx = i
#     for j in range(i + 1, n):
#         if num_list[j] < min:
#             min = num_list[j]
#             idx = j
#     if min != num_list[i]:
#         temp = num_list[i]
#         num_list[idx] = temp
#         num_list[i] = min 
# for num in num_list:
#     print(num)

