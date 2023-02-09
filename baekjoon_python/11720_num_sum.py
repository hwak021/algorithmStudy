n = int(input())
num = int(input())
num_str = str(num)
num_list = list(num_str)
tot = 0
for char in num_list:
    tot = tot + int(char)
print(str(tot))