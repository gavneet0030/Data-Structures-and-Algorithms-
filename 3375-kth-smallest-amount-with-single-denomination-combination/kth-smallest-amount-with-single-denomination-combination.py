from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        arr = []
        for c in coins:
            ok = True
            for x in arr:
                if c % x == 0:
                    ok = False
                    break
            if ok:
                arr.append(c)
        m = len(arr)
        subsets = []
        for mask in range(1, 1 << m):
            l = 1
            bits = 0
            valid = True
            for i in range(m):
                if mask & (1 << i):
                    bits += 1
                    l = l * arr[i] // gcd(l, arr[i])
                    if l > 10**18:
                        valid = False
                        break
            if valid:
                sign = 1 if bits % 2 else -1
                subsets.append((l, sign))

        def count(x: int) -> int:
            total = 0
            for l, sign in subsets:
                total += sign * (x // l)
            return total

        left, right = 1, arr[0] * k
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left