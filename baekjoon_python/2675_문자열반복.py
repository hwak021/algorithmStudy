n = int(input())
for i in range(n):
    str_list = list(map(str, input().split()))
    length = int(str_list[0])
    str1 = str_list[1]
    for char in str1:
        for j in range(length):
            print(char, end="")
    print("")