class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = []
        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                vals = set()
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.add(grid[x][y])
                if len(vals) <= 1:
                    row.append(0)
                else:
                    arr = sorted(vals)
                    mn = float("inf")
                    for t in range(1, len(arr)):
                        mn = min(mn, arr[t] - arr[t - 1])
                    row.append(mn)
            ans.append(row)
        return ans