class SparseTable:
    def __init__(self, nums):
        n = len(nums)

        self.log = [0] * (n + 1)

        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1

        k = self.log[n] + 1

        self.st = [[0] * n for _ in range(k)]

        self.st[0] = nums[:]

        for j in range(1, k):
            length = 1 << j

            for i in range(n - length + 1):
                self.st[j][i] = max(
                    self.st[j - 1][i],
                    self.st[j - 1][i + (length >> 1)]
                )

    def query(self, left, right):
        if left > right:
            return 0

        length = right - left + 1
        j = self.log[length]

        return max(
            self.st[j][left],
            self.st[j][right - (1 << j) + 1]
        )


class Solution:
    def maxActiveSectionsAfterTrade(self, s, queries):

        n = len(s)
        ones = s.count('1')


        zeroGroups = []
        zeroGroupIndex = []

        for i in range(n):

            if s[i] == '0':

                if i > 0 and s[i - 1] == '0':
                    zeroGroups[-1][1] += 1

                else:
        
                    zeroGroups.append([i, 1])

            zeroGroupIndex.append(len(zeroGroups) - 1)


        if len(zeroGroups) < 2:
            return [ones] * len(queries)

        merge = []

        for i in range(len(zeroGroups) - 1):
            merge.append(
                zeroGroups[i][1] +
                zeroGroups[i + 1][1]
            )

        st = SparseTable(merge)

        answer = []


        for l, r in queries:

            leftGroup = zeroGroupIndex[l]
            rightGroup = zeroGroupIndex[r]

            if leftGroup == -1:
                left = -1
            else:
                start, length = zeroGroups[leftGroup]
                left = length - (l - start)

            if rightGroup == -1:
                right = -1
            else:
                start, length = zeroGroups[rightGroup]
                right = r - start + 1

            startGroup = leftGroup + 1

            if s[r] == '1':
                endGroup = rightGroup
            else:
                endGroup = rightGroup - 1

            best = ones

            if (
                s[l] == '0' and
                s[r] == '0' and
                startGroup == rightGroup
            ):
                best = max(
                    best,
                    ones + left + right
                )


            elif startGroup <= endGroup - 1:

                gain = st.query(
                    startGroup,
                    endGroup - 1
                )

                best = max(
                    best,
                    ones + gain
                )


            if (
                s[l] == '0' and
                startGroup <= endGroup
            ):
                gain = (
                    left +
                    zeroGroups[startGroup][1]
                )

                best = max(
                    best,
                    ones + gain
                )

            if (
                s[r] == '0' and
                startGroup <= endGroup
            ):
                gain = (
                    right +
                    zeroGroups[endGroup][1]
                )

                best = max(
                    best,
                    ones + gain
                )

            answer.append(best)

        return answer