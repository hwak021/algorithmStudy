while True:
    try:
        num1, num2 = map(int, input().split())
        print(str(num1+num2))
    except EOFError:
        break