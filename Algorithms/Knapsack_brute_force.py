def knapsack(values, weights, capacity, i):
    if capacity <= 0 or i >= len(weights):
        return 0

    p1 = 0
    if weights[i] <= capacity:
        p1 = values[i] + knapsack(values, weights, capacity - weights[i], i+1)
    p2 = knapsack(values, weights, capacity, i+1)

    return max(p1, p2)

if __name__ == '__main__':
    ans = knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7, 0)
    print(ans)