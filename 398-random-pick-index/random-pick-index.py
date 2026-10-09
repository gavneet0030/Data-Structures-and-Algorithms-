import random

class Solution:
    def __init__(self, nums):
        self.indices = {}

        for i, num in enumerate(nums):
            self.indices.setdefault(num, []).append(i)

    def pick(self, target):
        return random.choice(self.indices[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)