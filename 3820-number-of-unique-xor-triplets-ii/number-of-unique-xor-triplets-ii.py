class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        vals = list(set(nums))

        MAX = 2048

        pair = [False] * MAX
        for a in vals:
            for b in vals:
                pair[a ^ b] = True

        ans = [False] * MAX
        for x in range(MAX):
            if pair[x]:
                for v in vals:
                    ans[x ^ v] = True

        return sum(ans)