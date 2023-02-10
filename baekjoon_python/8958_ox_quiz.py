n = int(input())
for i in range(n):
    ox_str = input()
    tot_score = 0
    score = 0
    for char in ox_str:
        if char == "O":
            score = score + 1
            tot_score = tot_score + score
        else:
            score = 0
    print(tot_score)
