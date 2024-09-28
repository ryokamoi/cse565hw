import math

mod = 10 ** 9 + 7

n = int(input())
a = list(map(int, input().split()))

a = [0] + a  # 1-indexed

# c[i]: the number of sequences where length is i, i-th value is a_k where k <= j
c = [0 for _ in range(n + 1)]

# initialization: j=1
c[0] = 1
c[1] = 1

# DP - Memory error
# for j in range(2, n + 1):
#     for i in range(1, n + 1):
#         if a[j] % i != 0:  # not divisible by i
#             c[i][j] = c[i][j - 1]
#         else:
#             c[i][j] = c[i][j - 1] + c[i - 1][j - 1]

# # DP -- TLE
# for j in range(2, n + 1):
#     for i in range(n, 0, -1):
#         if a[j] % i != 0:  # not divisible by i
#             c[i] = c[i]  # c[i][j] = c[i][j - 1]
#         else:
#             c[i] = (c[i] + c[i-1]) % mod


def find_divisors(n):
    small_divisors = []
    large_divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            small_divisors.append(i)
            if i != n // i:
                large_divisors.append(n // i)
    
    return small_divisors + large_divisors[::-1]

# DP
for j in range(2, n + 1):
    divisors = find_divisors(a[j])
    for i in divisors[::-1]:
        if i <= n:
            c[i] = (c[i] + c[i-1]) % mod

ans = 0
for i in range(1, n + 1):
    ans = (ans + c[i]) % mod

print(ans)
