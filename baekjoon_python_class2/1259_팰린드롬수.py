while True:
    num = int(input())
    if num == 0:
        break
    num_list = list(str(num))
    reversed_num_list = num_list[::-1]
    if num == int(''.join(reversed_num_list)):
        print("yes")
    else:
        print("no")