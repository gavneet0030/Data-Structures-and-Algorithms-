from typing import List

class Solution:
    def validPath(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int
    ) -> bool:
        parent = list(range(n))
        rank = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return

            if rank[root_a] < rank[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            rank[root_a] += rank[root_b]

        for u, v in edges:
            union(u, v)

        return find(source) == find(destination)