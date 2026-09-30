from typing import List
from collections import defaultdict, deque

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        mx = max(nums)

        spf = list(range(mx + 1))
        for i in range(2, int(mx ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, mx + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        prime_indices = defaultdict(list)

        for i, x in enumerate(nums):
            while x > 1:
                p = spf[x]
                prime_indices[p].append(i)
                while x % p == 0:
                    x //= p

        dist = [-1] * n
        dist[0] = 0
        q = deque([0])
        used = set()

        while q:
            i = q.popleft()
            d = dist[i]

            if i == n - 1:
                return d

            if i - 1 >= 0 and dist[i - 1] == -1:
                dist[i - 1] = d + 1
                q.append(i - 1)

            if i + 1 < n and dist[i + 1] == -1:
                dist[i + 1] = d + 1
                q.append(i + 1)

            p = nums[i]

            if p >= 2 and spf[p] == p and p not in used:
                used.add(p)

                for j in prime_indices[p]:
                    if dist[j] == -1:
                        dist[j] = d + 1
                        q.append(j)

        return -1