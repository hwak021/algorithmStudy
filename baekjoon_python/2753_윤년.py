num = int(input())
check = False
if (num % 4) == 0:
    if (num % 100) != 0 or (num % 400) == 0:
        check = True
if check:
    print(1)
else:
    print(0)