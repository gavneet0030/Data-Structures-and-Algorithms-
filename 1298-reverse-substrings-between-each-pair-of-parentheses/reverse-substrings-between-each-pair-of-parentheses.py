class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]

        for ch in s:
            if ch == '(':
                stack.append([])
            elif ch == ')':
                temp = stack.pop()
                stack[-1].extend(temp[::-1])
            else:
                stack[-1].append(ch)

        return ''.join(stack[0])