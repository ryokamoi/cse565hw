n = int(input())
a = list(map(int, input().split()))

a = [0] + a  # 1-indexed

# c[j]: the number of sequences where length is i, i-th value is a_k where k <= j
# initialize n+1 list with 0
c = [0 for _ in range(n + 1)]
c_prev = [0 for _ in range(n + 1)]

# initialization
for j in range(1, n + 1):
    c_prev[j] = c_prev[j - 1] + 1

# DP - Memory error
# for i in range(2, n + 1):
#     for j in range(1, n + 1):
#         if a[j] % i != 0:  # not divisible by i
#             c[i][j] = c[i][j - 1]
#         else:
#             c[i][j] = c[i][j - 1] + c[i - 1][j - 1]

# DP
ans = c_prev[n]
for i in range(2, n + 1):
    for j in range(1, n + 1):
        if a[j] % i != 0:  # not divisible by i
            c[j] = c[j - 1]
        else:
            c[j] = c[j - 1] + c_prev[j - 1]

    ans += c[n]
    for j in range(1, n + 1):
        c_prev[j] = c[j]

print(ans)
