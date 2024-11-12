def knapsack(values, weights, max_weight):
    n = len(values)
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
                
    return dp[n][max_weight]
    
# Example usage
values = [28, 24, 15]
weights = [18, 15, 10]
max_weight = 20

print("Max profit is:", knapsack(values, weights, max_weight))
