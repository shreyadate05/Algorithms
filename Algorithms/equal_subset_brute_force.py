
def canPartition_recursive(arr, s, i):
    if i >= len(arr) or s < 0:
        return False

    if s == 0:
        return True

    b1 = True
    if arr[i] <= s:
        b1 = canPartition_recursive(arr, s-arr[i], i+1)
    b2 = canPartition_recursive(arr, s, i+1)

    return b1 or b2

def canPartition(arr):
    if sum(arr) % 2 != 0:
        return False
    s = sum(arr)/2
    return canPartition_recursive(arr, s, 0)


if __name__ == "__main__":
    ans = canPartition([1,2,3,4])
    print(ans)