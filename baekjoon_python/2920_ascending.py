num_list = list(map(int, input().split()))
asc= False
desc = False
pre = 0
for n in num_list:
    if pre != 0:
        if pre > n:
            desc = True
        else:
            asc = True
        if asc == desc == True:
            print("mixed")
            asc = False
            desc = False
            break
    pre = n
if asc:
    print("ascending")
elif desc:
    print("descending")
    