n = 81
k = 10
partial_perm = 1
for i in range(k):
    partial_perm *= (n - i)
print(partial_perm % 1000000)