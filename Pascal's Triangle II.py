class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1], [1, 1]]

        if rowIndex < 2:
            return dp[rowIndex]

        for i in range(2, rowIndex + 1):
            arr = [0] * (i + 1)
            arr[0] = 1
            arr[len(arr) - 1] = 1
            dp.append(arr)
            for j in range(1, len(dp[i]) - 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

        return dp[rowIndex]


