n = int(input())

time = [0]
for _ in range(n):
    time.append(int(input()) + 1)  # 1-based

# optimal answer for each time
dp = [0 for _ in range(len(time) + 1)]


def binary_search_index(target_time):
    left = 0
    right = len(time) - 1
    possible_answer = 0

    # if there is no target_time in time, return the index of the largest time smaller than target_time
    while left <= right:
        mid = (left + right) // 2
        
        if time[mid] == target_time:
            return mid
        
        if time[mid] < target_time:
            possible_answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return possible_answer


for i in range(1, len(time)):
    # print("time", t)
    
    dp[i] = dp[i-1] + 20
    
    ninety_min_idx = binary_search_index(max(0, time[i]-90))
    # print("time", time[i])
    # print("ninety_min_idx", ninety_min_idx, time[ninety_min_idx])
    dp[i] = min(dp[i], dp[ninety_min_idx] + 50)
    
    oneday_idx = binary_search_index(max(0, time[i]-1440))
    dp[i] = min(dp[i], dp[oneday_idx] + 120)
    
    print(dp[i] - dp[i-1])
