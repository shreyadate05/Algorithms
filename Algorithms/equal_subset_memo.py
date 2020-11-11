
def canPartition_recursive(dp, arr, s, i):
    if s == 0:
        return 1

    if i >= len(arr) or len(arr) == 0:
        return 0

    if dp[i][s] == -1:
        if arr[i] <= s:
            if canPartition_recursive(dp, arr, s-arr[i], i+1):
                dp[i][s] = 1
            else:
                dp[i][s] = canPartition_recursive(dp, arr, s, i+1)

    return dp[i][s]

def canPartition(arr):
    if sum(arr) % 2 != 0:
        return 0

    s = int(sum(arr)/2)
    dp = [[-1 for j in range(s+1)] for i in range(len(arr))]
    ans = canPartition_recursive(dp, arr, s, 0)
    print(dp)
    return ans

if __name__ == "__main__":
    ans = canPartition([1,2,3,4])
    print(ans)
    # [[-1, -1, -1, -1, -1, 1], [-1, -1, -1, -1, 1, -1], [-1, -1, 0, -1, 1, -1], [-1, 0, 0, -1, 1, -1]]