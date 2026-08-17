class Solution:
    def permute(self, nums):
        ans = []
        path = []
        used = [False] * len(nums)
        def backtrack():
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False
        backtrack()
        return ans