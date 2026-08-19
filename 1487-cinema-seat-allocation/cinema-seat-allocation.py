class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}
        for r, s in reservedSeats:
            rows[r] = rows.get(r, 0) | (1 << (s - 1))
        left = 0
        for x in [2,3,4,5]:
            left |= 1 << (x - 1)
        mid = 0
        for x in [4,5,6,7]:
            mid |= 1 << (x - 1)
        right = 0
        for x in [6,7,8,9]:
            right |= 1 << (x - 1)
        ans = (n - len(rows)) * 2
        for mask in rows.values():
            left_free = (mask & left) == 0
            mid_free = (mask & mid) == 0
            right_free = (mask & right) == 0
            if left_free and right_free:
                ans += 2
            elif left_free or mid_free or right_free:
                ans += 1
        return ans