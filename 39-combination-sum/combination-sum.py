class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        path = []
        def dfs(i, remaining):
            if remaining == 0:
                ans.append(path[:])
                return
            if i == len(candidates) or remaining < 0:
                return
            path.append(candidates[i])
            dfs(i, remaining - candidates[i])  
            path.pop()
            dfs(i + 1, remaining)
        dfs(0, target)
        return ans