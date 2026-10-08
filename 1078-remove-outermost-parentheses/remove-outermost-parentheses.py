class Solution:
    def removeOuterParentheses(self, s):
        ans = []
        balance = 0

        for c in s:
            if c == '(':
                if balance > 0:
                    ans.append(c)
                balance += 1
            else:
                balance -= 1
                if balance > 0:
                    ans.append(c)

        return ''.join(ans)