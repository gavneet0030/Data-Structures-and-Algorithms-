class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        arr = sorted((nums[i], i) for i in range(n))

        result = [0] * n
        start = 0

        while start < n:
            end = start

            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            positions = sorted(arr[i][1] for i in range(start, end + 1))
            values = [arr[i][0] for i in range(start, end + 1)]
            for pos, value in zip(positions, values):
                result[pos] = value

            start = end + 1

        return result