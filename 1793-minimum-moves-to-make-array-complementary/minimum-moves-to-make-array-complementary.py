class Solution:
    def minMoves(self, nums, limit):
        diff = [0] * (2 * limit + 2)
        n = len(nums)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit
            total = a + b

            diff[low] -= 1
            diff[high + 1] += 1

            diff[total] -= 1
            diff[total + 1] += 1

        moves = n
        ans = n

        for s in range(2, 2 * limit + 1):
            moves += diff[s]
            ans = min(ans, moves)

        return ans