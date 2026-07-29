from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        LIMIT = 10**6 + 1

        freq = Counter(s)
        mid = ""
        half = [0] * 26

        for ch, cnt in freq.items():
            if cnt % 2:
                mid = ch
            half[ord(ch) - 97] = cnt // 2

        def count_perms(cnts):
            rem = sum(cnts)
            res = 1
            for c in cnts:
                if c:
                    res *= comb(rem, c)
                    if res >= LIMIT:
                        return LIMIT
                    rem -= c
            return res

        if count_perms(half) < k:
            return ""

        left = []
        total = sum(half)

        for _ in range(total):
            for i in range(26):
                if half[i] == 0:
                    continue
                half[i] -= 1
                ways = count_perms(half)
                if ways >= k:
                    left.append(chr(i + 97))
                    break
                k -= ways
                half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]