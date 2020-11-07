s1 = "blue"
s2 = "clues"
dp = [[0 for j in range(len(s2))] for i in range(len(s1))]

def get_max(dp):
    temp = []
    for row in dp:
        for n in row:
            temp.append(n)
    return max(temp)

def find_longest_common_substring(dp):
    dp[0][0] = int(s1[0] == s2[0])
    for i in range(len(dp[0])):
        if s2[i] == s1[0]:
            dp[0][i] = 1
        else:
            dp[0][i] = dp[0][i - 1]

    for i in range(len(dp)):
        if s2[0] == s1[i]:
            dp[i][0] = 1
        else:
            dp[i][0] = dp[i - 1][0]

    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 0

    return get_max(dp)

def setup():
    global s1, s2
    s1 = input("Enter string 1: ")
    s2 = input("Enter string 2: ")
    dp = [[0 for j in range(len(s2))] for i in range(len(s1))]
    return dp

if __name__ == '__main__':
    #dp = setup()
    ans = find_longest_common_substring(dp)
    print(dp)
    print("Length of longest common substring is: ", ans)