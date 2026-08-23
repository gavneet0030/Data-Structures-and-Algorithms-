class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        leftSum = rightSum = 0
        leftQ = rightQ = 0
        for i in range(half):
            if num[i] == '?':
                leftQ += 1
            else:
                leftSum += int(num[i])
        for i in range(half, n):
            if num[i] == '?':
                rightQ += 1
            else:
                rightSum += int(num[i])
        if (leftQ + rightQ) % 2 == 1:
            return True

        diff = leftSum - rightSum
        return 2 * diff != 9 * (rightQ - leftQ)