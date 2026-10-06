class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        total = sum(nums)

        f = sum(i * nums[i] for i in range(n))
        ans = f

        for k in range(1, n):
            f += total - n * nums[n - k]
            ans = max(ans, f)

        return ans