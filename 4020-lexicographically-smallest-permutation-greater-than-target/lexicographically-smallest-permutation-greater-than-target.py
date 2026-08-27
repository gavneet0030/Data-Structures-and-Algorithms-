class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        best = ""

        for i in range(n):
            count = [0] * 26

            for ch in s:
                count[ord(ch) - ord('a')] += 1

            possible = True

            for j in range(i):
                c = ord(target[j]) - ord('a')

                if count[c] == 0:
                    possible = False
                    break

                count[c] -= 1

            if not possible:
                continue

            c = ord(target[i]) - ord('a')
            bigger = -1

            for x in range(c + 1, 26):
                if count[x] > 0:
                    bigger = x
                    break

            if bigger == -1:
                continue

            count[bigger] -= 1

            suffix = []

            for x in range(26):
                while count[x] > 0:
                    suffix.append(chr(x + ord('a')))
                    count[x] -= 1

            candidate = (
                target[:i]
                + chr(bigger + ord('a'))
                + ''.join(suffix)
            )

            if best == "" or candidate < best:
                best = candidate

        return best