class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        best_gain = 0
        t = '1' + s + '1'

        i = 1

        while i < len(t) - 1:
            if t[i] == '0':
                start = i

                while i < len(t) and t[i] == '0':
                    i += 1

                zero_len = i - start
                left_zero = zero_len

                if i < len(t) and t[i] == '1':
                    j = i

                    while j < len(t) and t[j] == '1':
                        j += 1
                    if j < len(t) and t[j] == '0':
                        k = j

                        while k < len(t) and t[k] == '0':
                            k += 1

                        right_zero = k - j

                        best_gain = max(
                            best_gain,
                            left_zero + right_zero
                        )

                    i = j
            else:
                i += 1

        return ones + best_gain