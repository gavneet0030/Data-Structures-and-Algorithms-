from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                value = grid[i][j]

                if i > 0:
                    dp[i][j].update(x ^ value for x in dp[i - 1][j])

                if j > 0:
                    dp[i][j].update(x ^ value for x in dp[i][j - 1])

        return min(dp[m - 1][n - 1])