class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []

        if not nums:
            return ans

        start = nums[0]

        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                end = nums[i - 1]

                if start == end:
                    ans.append(str(start))
                else:
                    ans.append(f"{start}->{end}")

                if i < len(nums):
                    start = nums[i]

        return ans