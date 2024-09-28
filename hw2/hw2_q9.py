n = int(input())

time = []
for _ in range(n):
    time.append(int(input()) + 1)  # 1-based

time_bool = [False for _ in range(max(time)+1)]
for t in time:
    time_bool[t] = True

# optimal answer for each time
dp = [0 for _ in range(max(time)+1)]


for t in range(max(time)+1):
    if not time_bool[t]:
        if t >= 1:
            dp[t] = dp[t-1]
        continue
    
    # print("time", t)
    
    dp[t] = dp[t-1] + 20
    dp[t] = min(dp[t], dp[t-min(90, t)] + 50)
    dp[t] = min(dp[t], dp[t-min(1440, t)] + 120)
    
    print(dp[t] - dp[t-1])

# print(dp)
