from typing import List
from functools import lru_cache
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        @lru_cache(None)
        def dp(i: int, g1: int, g2: int) -> int:
            if i == n:
                return 1 if g1 != 0 and g1 == g2 else 0

            ans = dp(i + 1, g1, g2)

            new_g1 = nums[i] if g1 == 0 else gcd(g1, nums[i])
            ans += dp(i + 1, new_g1, g2)

            new_g2 = nums[i] if g2 == 0 else gcd(g2, nums[i])
            ans += dp(i + 1, g1, new_g2)

            return ans % MOD

        return dp(0, 0, 0)