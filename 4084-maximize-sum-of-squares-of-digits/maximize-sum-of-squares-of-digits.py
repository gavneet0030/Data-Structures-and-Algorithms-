class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""

        q, r = divmod(sum, 9)
        result = "9" * q

        if r > 0:
            result += str(r)

        result += "0" * (num - len(result))
        return result