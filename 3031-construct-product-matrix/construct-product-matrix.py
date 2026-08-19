class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        size = n * m
        arr = [0] * size
        k = 0
        for i in range(n):
            for j in range(m):
                arr[k] = grid[i][j] % MOD
                k += 1
        res = [1] * size
        prefix = 1
        for i in range(size):
            res[i] = prefix
            prefix = (prefix * arr[i]) % MOD
        suffix = 1
        for i in range(size - 1, -1, -1):
            res[i] = (res[i] * suffix) % MOD
            suffix = (suffix * arr[i]) % MOD
        ans = [[0] * m for _ in range(n)]
        k = 0
        for i in range(n):
            for j in range(m):
                ans[i][j] = res[k]
                k += 1
        return ans