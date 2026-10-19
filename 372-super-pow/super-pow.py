class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337

        def power(x, n):
            result = 1
            x %= MOD

            while n:
                if n & 1:
                    result = result * x % MOD
                x = x * x % MOD
                n >>= 1

            return result

        result = 1
        for digit in b:
            result = power(result, 10) * power(a, digit) % MOD

        return result