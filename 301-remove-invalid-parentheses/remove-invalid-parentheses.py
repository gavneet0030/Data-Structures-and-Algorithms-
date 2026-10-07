class Solution:
    def removeInvalidParentheses(self, s):
        def valid(t):
            balance = 0

            for c in t:
                if c == '(':
                    balance += 1
                elif c == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        level = {s}

        while level:
            ans = [x for x in level if valid(x)]

            if ans:
                return ans

            next_level = set()

            for x in level:
                for i in range(len(x)):
                    if x[i] in '()':
                        next_level.add(x[:i] + x[i + 1:])

            level = next_level

        return [""]