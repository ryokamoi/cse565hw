t = int(input())

problems = []
for _ in range(t):
    a, b = map(int, input().split())
    problems.append((a, b))

# get all prime numbers up to max_num
max_num = 5000000
is_prime = [True for _ in range(max_num + 1)]
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(max_num ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, max_num + 1, i):
            is_prime[j] = False

# get all prime numbers up to max_num
prime_numbers = [i for i in range(max_num + 1) if is_prime[i]]

# sum of all prime factors up to max_num
num_prime_factors = [0 for _ in range(max_num + 1)]
def count_prime_factors(num):
    if num <= 1:
        return 0
    
    if is_prime[num]:
        return 1
    
    for prime in prime_numbers:
        if num % prime == 0:
            return 1 + num_prime_factors[num // prime]


sum_of_prime_factors = [0 for _ in range(max_num + 1)]
for a in range(2, max_num + 1):
    num_prime_factors[a] = count_prime_factors(a)
    sum_of_prime_factors[a] = sum_of_prime_factors[a - 1] + num_prime_factors[a]

# print([sum_of_prime_factors[i] for i in range(10)])
# print([count_prime_factors(i) for i in range(10)])
for a, b in problems:
    print(sum_of_prime_factors[a] - sum_of_prime_factors[b])
