class Solution:
    def longestSubstring(self, s, k):
        def solve(l, r):
            if r - l < k:
                return 0

            count = [0] * 26
            for i in range(l, r):
                count[ord(s[i]) - 97] += 1

            for i in range(l, r):
                if count[ord(s[i]) - 97] < k:
                    return max(solve(l, i), solve(i + 1, r))

            return r - l

        return solve(0, len(s))