t = int(input())

problems = []
for _ in range(t):
    a, b = map(int, input().split())
    problems.append((a, b))

# get all prime numbers up to max_num
max_num = 5000000
is_prime = [True for _ in range(max_num + 1)]
prime_factor = [0 for _ in range(max_num + 1)]
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(max_num ** 0.5) + 1):
    if is_prime[i]:
        prime_factor[i] = i
        for j in range(i * i, max_num + 1, i):
            is_prime[j] = False
            prime_factor[j] = i

# print("done1")

# get all prime numbers up to max_num
prime_numbers = [i for i in range(max_num + 1) if is_prime[i]]

# count num of prime factors
num_prime_factors = [0 for _ in range(max_num + 1)]
for a in range(2, max_num + 1):
    if is_prime[a]:
        num_prime_factors[a] = 1
        continue
    
    # for prime in prime_numbers:
    #     if a % prime == 0:
    #         num_prime_factors[a] = 1 + num_prime_factors[a // prime]
    #         break
    num_prime_factors[a] = 1 + num_prime_factors[a // prime_factor[a]]

# print("done2")

# sum of all prime factors up to max_num
sum_of_prime_factors = [0 for _ in range(max_num + 1)]
for a in range(2, max_num + 1):
    sum_of_prime_factors[a] = sum_of_prime_factors[a - 1] + num_prime_factors[a]

# print([sum_of_prime_factors[i] for i in range(10)])
# print([count_prime_factors(i) for i in range(10)])
for a, b in problems:
    print(sum_of_prime_factors[a] - sum_of_prime_factors[b])
