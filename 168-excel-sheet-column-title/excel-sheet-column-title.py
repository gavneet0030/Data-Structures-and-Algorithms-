class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []

        while columnNumber > 0:
            columnNumber -= 1
            ans.append(chr(ord('A') + columnNumber % 26))
            columnNumber //= 26

        return "".join(reversed(ans))