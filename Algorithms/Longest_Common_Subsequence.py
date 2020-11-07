s1 = "abcde"
s2 = "abc"
dp = [[0 for j in range(len(s2))] for i in range(len(s1))]

def find_longest_common_subsequence(dp):
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
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[len(s1)-1][len(s2)-1]

def setup():
    global s1, s2
    s1 = input("Enter string 1: ")
    s2 = input("Enter string 2: ")
    dp = [[0 for j in range(len(s2))] for i in range(len(s1))]
    return dp

if __name__ == '__main__':
    #dp = setup()
    ans = find_longest_common_subsequence(dp)
    print(dp)
    print("Length of longest common subsequence is: ", ans)