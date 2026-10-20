class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for bit in range(31):
            ones = sum((num >> bit) & 1 for num in nums)
            zeros = n - ones
            ans += ones * zeros

        return ans