capacity = 4
items = ['water', 'book', 'food', 'jacket', 'camera']
weights = [3, 1, 2, 2, 1]
values = [10, 3, 9, 5, 6]
dp = [[0 for j in range(capacity+1)] for i in range(len(items))]

def knapsack():
    for i in range(len(weights)):
        dp[i][0] = 0

    for i in range(capacity+1):
        if weights[0] <= i:
            dp[0][i] = values[0]

    for i in range(len(weights)):
        for j in range(1,capacity+1):
            weight = weights[i]
            value  = 0
            if weights[i] <= j:
                value = values[i] + dp[i-1][j-weight]
            dp[i][j] = max(dp[i-1][j], value)

    print(dp)

def setup():
    capacity = input("Enter knapsack capacity: ")
    choice = input("\nMENU: \n1. Add Item \n2.Stop \nEnter choice: ")
    while choice == "1":
        items.append(int(input("Enter item name: ")))
        weights.append(int(input("Enter item weight: ")))
        values.append(int(input("Enter item value: ")))
        choice = input("\nMENU: \n1. Add Item \n2.Stop \nEnter choice: ")
    return

if __name__ == '__main__':
    #setup()
    print(items)
    print(weights)
    print(values)
    print(dp)
    knapsack()
