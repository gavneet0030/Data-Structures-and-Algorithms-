from bisect import bisect_right
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = [
            [l, r, w, i]
            for i, (l, r, w) in enumerate(intervals)
        ]
        arr.sort()

        starts = [x[0] for x in arr]
        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])
        memo = {}

        def solve(i, k):
            if i >= n or k == 0:
                return (0, ())

            if (i, k) in memo:
                return memo[(i, k)]
            best = solve(i + 1, k)
            score, indices = solve(nxt[i], k - 1)

            candidate_score = arr[i][2] + score
            candidate_indices = tuple(sorted(indices + (arr[i][3],)))
            if candidate_score > best[0] or (
                candidate_score == best[0]
                and candidate_indices < best[1]
            ):
                best = (candidate_score, candidate_indices)

            memo[(i, k)] = best
            return best

        return list(solve(0, 4)[1])