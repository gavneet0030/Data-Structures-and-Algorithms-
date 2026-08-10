class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        n = len(num1)
        m = len(num2)

        result = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                x = int(num1[i])
                y = int(num2[j])

                product = x * y

                pos1 = i + j
                pos2 = i + j + 1

                result[pos2] += product

                result[pos1] += result[pos2] // 10
                result[pos2] %= 10

        # Remove leading zeros
        i = 0
        while i < len(result) and result[i] == 0:
            i += 1

        return ''.join(map(str, result[i:]))