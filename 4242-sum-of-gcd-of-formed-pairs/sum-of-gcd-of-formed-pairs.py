from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []

        prefixMax = 0
        for x in nums:
            prefixMax = max(prefixMax, x)
            prefixGcd.append(gcd(x, prefixMax))

        prefixGcd.sort()

        ans = 0
        left, right = 0, len(prefixGcd) - 1

        while left < right:
            ans += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return ans