length = int(input())
score_list = list(map(int, input().split()))
max_score = max(score_list)
tot = []
for score in score_list:
    tot.append(score/max_score*100)
avg = sum(tot)/length
print(avg)