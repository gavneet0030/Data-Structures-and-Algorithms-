class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        odd = [i for i in range(26) if cnt[i] % 2]
        if len(odd) > 1:
            return ""

        mid = "" if not odd else chr(odd[0] + ord('a'))
        half_cnt = [x // 2 for x in cnt]
        h = n // 2

        def build(left):
            return left + mid + left[::-1]
        rem = half_cnt[:]
        prefix = []

        for i in range(h):
            c = ord(target[i]) - ord('a')

            if rem[c] == 0:
                break

            rem[c] -= 1
            prefix.append(target[i])
        else:
            candidate = build(''.join(prefix))

            if candidate > target:
                return candidate
        for i in range(h - 1, -1, -1):
            rem = half_cnt[:]

            possible = True

            for j in range(i):
                c = ord(target[j]) - ord('a')

                if rem[c] == 0:
                    possible = False
                    break

                rem[c] -= 1

            if not possible:
                continue

            current = ord(target[i]) - ord('a')

            bigger = -1

            for c in range(current + 1, 26):
                if rem[c] > 0:
                    bigger = c
                    break

            if bigger == -1:
                continue

            rem[bigger] -= 1

            left = target[:i] + chr(bigger + ord('a'))

            for c in range(26):
                left += chr(c + ord('a')) * rem[c]

            return build(left)

        return ""