class Solution:
    def isNumber(self, s: str) -> bool:
        digit = False
        dot = False
        e = False
        digitAfterE = True

        for i, ch in enumerate(s):

            if ch.isdigit():
                digit = True

                if e:
                    digitAfterE = True
            elif ch == '.':
                if dot or e:
                    return False

                dot = True
            elif ch == 'e' or ch == 'E':
                if e or not digit:
                    return False

                e = True
                digitAfterE = False

            elif ch == '+' or ch == '-':
                if i != 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False

            else:
                return False

        return digit and digitAfterE