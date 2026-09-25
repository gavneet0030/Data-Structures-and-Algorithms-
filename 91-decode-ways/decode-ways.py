class Solution:
    def numDecodings(self, s: str) -> int:
        prev2 = 1
        prev1 = 1

        for i in range(1, len(s) + 1):
            curr = 0

            if s[i - 1] != '0':
                curr += prev1

            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                curr += prev2

            prev2 = prev1
            prev1 = curr

        return prev1