class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digitProduct(num):
            product = 1
            while num > 0:
                product *= num % 10
                num //= 10
            return product

        while True:
            if digitProduct(n) % t == 0:
                return n
            n += 1