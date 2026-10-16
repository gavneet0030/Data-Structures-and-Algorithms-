class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        size = 4 * n
        tree = [0] * size
        lazy = [0] * size
        ans = 0
        last = {}

        def apply(node, start, end, val):
            length = end - start + 1
            tree[node] = (tree[node] + 2 * val * tree_sum[node] + val * val * length) % MOD
            tree_sum[node] = (tree_sum[node] + val * length) % MOD
            lazy[node] += val

        tree_sum = [0] * size

        def push(node, start, end):
            if lazy[node] == 0 or start == end:
                return
            mid = (start + end) // 2
            val = lazy[node]
            apply(node * 2, start, mid, val)
            apply(node * 2 + 1, mid + 1, end, val)
            lazy[node] = 0

        def update(node, start, end, left, right):
            if left > end or right < start:
                return
            if left <= start and end <= right:
                apply(node, start, end, 1)
                return
            push(node, start, end)
            mid = (start + end) // 2
            update(node * 2, start, mid, left, right)
            update(node * 2 + 1, mid + 1, end, left, right)
            tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD
            tree_sum[node] = (tree_sum[node * 2] + tree_sum[node * 2 + 1]) % MOD

        for i, x in enumerate(nums):
            left = last.get(x, -1) + 1
            update(1, 0, n - 1, left, i)
            last[x] = i
            ans = (ans + tree[1]) % MOD

        return ans