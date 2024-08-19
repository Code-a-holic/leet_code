class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1], [1, 1]]

        if numRows < 2:
            return dp[0:numRows]

        for i in range(2, numRows):
            arr = [0] * (i + 1)
            arr[0] = 1
            arr[len(arr) - 1] = 1
            dp.append(arr)

            for j in range(1, len(arr) - 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

        return dp




