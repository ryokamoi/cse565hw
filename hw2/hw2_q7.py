n = int(input())
a = list(map(int, input().split()))

a = [0] + a  # 1-indexed

# c[i][j]: the number of sequences where length is i, i-th value is a_k where k <= j
# initialize n+1 x n+1 matrix with 0
c = [[0] * (n + 1) for _ in range(n + 1)]

# initialization
for j in range(1, n + 1):
    c[1][j] = c[1][j - 1] + 1

# DP
for i in range(2, n + 1):
    for j in range(1, n + 1):
        if a[j] % i != 0:  # not divisible by i
            c[i][j] = c[i][j - 1]
        else:
            c[i][j] = c[i][j - 1] + c[i - 1][j - 1]

# answer
ans = 0
for i in range(1, n + 1):
    ans += c[i][n]

print(ans)
