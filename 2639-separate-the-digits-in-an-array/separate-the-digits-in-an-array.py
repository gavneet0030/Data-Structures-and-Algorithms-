class Solution:
    def separateDigits(self, nums):
        ans = []

        for num in nums:
            ans.extend(map(int, str(num)))

        return ans