from typing import List

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = sum(p % 2 == 0 for p in position)
        odd = len(position) - even
        return min(even, odd)