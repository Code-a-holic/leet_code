class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        else:
            dp = [0] * n
            dp[n - 1] = 1
            dp[n - 2] = 2
            for i in range(n - 3, -1, -1):
                dp[i] = dp[i + 1] + dp[i + 2]

            return dp[0]


