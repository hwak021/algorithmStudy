num_list = []
mod_list = []
for i in range(10):
    num = int(input())
    num_list.append(num)
for num in num_list:
    mod_tmp = num % 42
    check = False
    for mod in mod_list:
        if mod == mod_tmp:
            check = True
    if not check:
        mod_list.append(mod_tmp)
print(len(mod_list))
