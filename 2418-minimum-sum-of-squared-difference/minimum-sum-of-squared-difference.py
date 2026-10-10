class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        diffs.sort(reverse=True)
        diffs.append(0)

        for i in range(len(diffs) - 1):
            need = (diffs[i] - diffs[i + 1]) * (i + 1)

            if k >= need:
                k -= need
            else:
                level, rem = divmod(k, i + 1)
                x = diffs[i] - level
                return (i + 1 - rem) * x * x + rem * (x - 1) * (x - 1) + sum(d * d for d in diffs[i + 1:])

        return sum(d * d for d in diffs)