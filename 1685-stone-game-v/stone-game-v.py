class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
        dp = [[-1] * n for _ in range(n)]
        def solve(l, r):
            if l == r:
                return 0
            if dp[l][r] != -1:
                return dp[l][r]
            ans = 0
            for k in range(l, r):
                left = prefix[k + 1] - prefix[l]
                right = prefix[r + 1] - prefix[k + 1]
                if left < right:
                    ans = max(ans, left + solve(l, k))
                elif left > right:
                    ans = max(ans, right + solve(k + 1, r))
                else:
                    ans = max(
                        ans,
                        left + max(solve(l, k), solve(k + 1, r))
                    )
            dp[l][r] = ans
            return ans
        return solve(0, n - 1)