
def canPartition(arr):
    if sum(arr) % 2 != 0:
        return False

    s = int(sum(arr)/2)
    dp = [[False for j in range(s+1)] for i in range(len(arr))]

    for i in range(s+1):
        dp[0][i] = (arr[0] == i)

    for i in range(len(arr)):
        dp[i][0] = True

    for i in range(len(arr)):
        for j in range(s+1):
            if arr[i] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i]]
            else:
                dp[i][j] = dp[i-1][j]

    print(dp)
    return dp[len(arr)-1][s]

if __name__ == "__main__":
    print(canPartition([1,2,3,4]))