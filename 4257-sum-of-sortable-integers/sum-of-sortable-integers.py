from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        target = sorted(nums)

        if nums == target:
            return sum(d for d in range(1, n + 1) if n % d == 0)

        mod1, mod2 = 1_000_000_007, 1_000_000_009
        base1, base2 = 911382323, 972663749

        vals = set(nums)
        h1 = {v: (v * base1 + 97266353) % mod1 for v in vals}
        h2 = {v: (v * base2 + 19260817) % mod2 for v in vals}

        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)
        targ1 = [0] * (n + 1)
        targ2 = [0] * (n + 1)

        for i, x in enumerate(nums):
            pref1[i + 1] = (pref1[i] + h1[x]) % mod1
            pref2[i + 1] = (pref2[i] + h2[x]) % mod2

        for i, x in enumerate(target):
            targ1[i + 1] = (targ1[i] + h1[x]) % mod1
            targ2[i + 1] = (targ2[i] + h2[x]) % mod2

        divisors = []
        d = 1
        while d * d <= n:
            if n % d == 0:
                divisors.append(d)
                if d * d != n:
                    divisors.append(n // d)
            d += 1

        ans = 0

        for k in divisors:
            valid = True

            for start in range(0, n, k):
                end = start + k


                if (
                    (pref1[end] - pref1[start]) % mod1
                    != (targ1[end] - targ1[start]) % mod1
                    or
                    (pref2[end] - pref2[start]) % mod2
                    != (targ2[end] - targ2[start]) % mod2
                ):
                    valid = False
                    break

                drops = 0
                for i in range(start, end - 1):
                    if nums[i] > nums[i + 1]:
                        drops += 1
                        if drops > 1:
                            break

                if drops > 1:
                    valid = False
                    break

                if nums[end - 1] > nums[start]:
                    drops += 1

                if drops > 1:
                    valid = False
                    break

            if valid:
                ans += k

        return ans