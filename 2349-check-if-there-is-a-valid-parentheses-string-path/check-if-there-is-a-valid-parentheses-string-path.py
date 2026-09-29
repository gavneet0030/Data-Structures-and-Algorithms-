from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        if (m + n) % 2 == 0:
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                for balance in (
                    (dp[i - 1][j] if i > 0 else set()) |
                    (dp[i][j - 1] if j > 0 else set())
                ):
                    new_balance = balance + (1 if grid[i][j] == '(' else -1)

                    if new_balance >= 0:
                        dp[i][j].add(new_balance)

        return 0 in dp[m - 1][n - 1]