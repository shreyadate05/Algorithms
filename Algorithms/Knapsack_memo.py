'''
We cannot have more than n*c sub problems.
So, Time Complexity: O(n*c) where n = number of items & c = capacity
Space Complexity: O(n*c + n) space for dp array = n*c and n recursion calls

'''

def knapsack(dp, values, weights, capacity, i):
    if capacity <= 0 or i >= len(weights):
        return 0

    if dp[i][capacity] != -1:
        return dp[i][capacity]

    p1 = 0
    if weights[i] <= capacity:
        p1 = values[i] + knapsack(dp, values, weights, capacity - weights[i], i+1)
    p2 = knapsack(dp, values, weights, capacity, i+1)

    dp[i][capacity] = max(p1, p2)
    return dp[i][capacity]

if __name__ == '__main__':
    capacity = 7
    profits = [1, 6, 10, 16]
    weights =  [1, 2, 3, 5]
    dp = [[-1 for j in range(capacity+1)] for i in range(len(weights))]

    ans = knapsack(dp, profits, weights, capacity, 0)
    print(ans)
