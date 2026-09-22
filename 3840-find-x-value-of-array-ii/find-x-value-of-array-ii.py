from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int,
                    queries: List[List[int]]) -> List[int]:

        n = len(nums)

        def make_node(value):
            x = value % k
            pref = [0] * k
            pref[x] = 1

            return [x, pref]

        def merge(A, B):
            totalA, prefA = A
            totalB, prefB = B

            total = (totalA * totalB) % k
            pref = prefA[:]

            # Prefixes that use all of A + a prefix of B
            for r in range(k):
                if prefB[r]:
                    pref[(totalA * r) % k] += prefB[r]

            return [total, pref]

        size = 1
        while size < n:
            size *= 2

        tree = [None] * (2 * size)

        for i in range(n):
            tree[size + i] = make_node(nums[i])

        for i in range(size - 1, 0, -1):
            left = tree[2 * i]
            right = tree[2 * i + 1]

            if left is None:
                tree[i] = right
            elif right is None:
                tree[i] = left
            else:
                tree[i] = merge(left, right)

        def update(pos, value):
            pos += size
            tree[pos] = make_node(value)

            pos //= 2

            while pos:
                left = tree[2 * pos]
                right = tree[2 * pos + 1]

                if left is None:
                    tree[pos] = right
                elif right is None:
                    tree[pos] = left
                else:
                    tree[pos] = merge(left, right)

                pos //= 2

        def query(left, right):
            left += size
            right += size

            left_result = None
            right_result = None

            while left < right:

                if left & 1:
                    if left_result is None:
                        left_result = tree[left]
                    else:
                        left_result = merge(left_result, tree[left])
                    left += 1

                if right & 1:
                    right -= 1
                    if right_result is None:
                        right_result = tree[right]
                    else:
                        right_result = merge(tree[right], right_result)

                left //= 2
                right //= 2

            if left_result is None:
                return right_result

            if right_result is None:
                return left_result

            return merge(left_result, right_result)

        ans = []

        for index, value, start, x in queries:
            nums[index] = value
            update(index, value)

            node = query(start, n)

            ans.append(node[1][x])

        return ans