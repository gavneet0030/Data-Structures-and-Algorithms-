class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]

        fact = 1
        for i in range(1, n):
            fact *= i

        k -= 1                 
        ans = []

        while nums:
            index = k // fact
            ans.append(nums.pop(index))

            k %= fact

            if not nums:
                break

            fact //= len(nums)

        return "".join(ans)