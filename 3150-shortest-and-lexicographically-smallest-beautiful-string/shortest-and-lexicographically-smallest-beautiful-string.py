class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        best = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1
            if ones == k:
                while s[left] == '0':
                    left += 1

                current = s[left:right + 1]

                if (not best or
                    len(current) < len(best) or
                    (len(current) == len(best) and current < best)):
                    best = current

                left += 1
                ones -= 1

        return best