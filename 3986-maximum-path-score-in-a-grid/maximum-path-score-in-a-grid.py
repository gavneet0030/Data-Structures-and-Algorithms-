from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[-1] * (k + 1) for _ in range(n)]

        for i in range(m):
            for j in range(n):
                value = grid[i][j]
                cost = 0 if value == 0 else 1

                if i == 0 and j == 0:
                    dp[j][cost] = value
                    continue

                prev = []

                if i > 0:
                    prev.append(dp[j])

                if j > 0:
                    prev.append(dp[j - 1])

                new = [-1] * (k + 1)

                for c in range(cost, k + 1):
                    best = -1

                    for p in prev:
                        if p[c - cost] != -1:
                            best = max(best, p[c - cost] + value)

                    new[c] = best

                dp[j] = new

        return max(dp[n - 1]) if max(dp[n - 1]) != -1 else -1