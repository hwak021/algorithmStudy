num_list = list(map(int, input().split()))
tot = 0
for n in num_list:
    tot = tot + (n * n)
mod = tot % 10
print(mod)