str = input().upper()
dict = {}
for i in str:
    if i not in dict:
        dict[i] = 1
    if i in dict:
        dict[i] = dict[i] + 1
key_list = list(dict.keys())
value_list = list(dict.values())
max_num = max(value_list)
count = value_list.count(max_num)

if count != 1: 
    print("?")
else:
    idx = value_list.index(max_num)
    chr = key_list[idx]
    print(chr)
