python
if wt[i-1] > w:
dp[i][w] = dp[i-1][w] # Cannot include the current item
else: # Choose the maximum of: # 1. Not taking the i-th item: value remains `dp[i-1][w]` # 2. Taking the i-th item: value is `val[i-1] + dp[i-1][w - wt[i-1]]`
dp[i][w] = max(dp[i-1][w], val[i-1] + dp[i-1]w - wt[i-1]])
