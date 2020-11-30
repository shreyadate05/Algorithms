def subset_sum(arr, k, i, temp, count):
    if i >= len(arr):
        return 0

    if sum(temp) == k:
        count += 1
        return

    if arr[i] <= k:
        b1 = subset_sum(arr, k-arr[i], i+1, count)
    b2 = subset_sum(arr, k, i+1, count)

def main():
    count = 0
    print(subset_sum([1,1,1], 2, 0, [], count))
    print(count)

main()