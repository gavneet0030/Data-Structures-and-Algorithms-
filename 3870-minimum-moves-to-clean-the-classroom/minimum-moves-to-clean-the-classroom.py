from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        litter_id = {}
        start = None
        litter_count = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = litter_count
                    litter_count += 1

        full_mask = (1 << litter_count) - 1

        if full_mask == 0:
            return 0


        q = deque()
        q.append((start[0], start[1], energy, 0, 0))
        best = {}

        best[(start[0], start[1], 0)] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, e, mask, moves = q.popleft()

            if mask == full_mask:
                return moves

            if e == 0 and classroom[r][c] != 'R':
                continue

            if classroom[r][c] == 'R':
                e = energy

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                if e <= 0:
                    continue

                ne = e - 1
                nmask = mask

                if classroom[nr][nc] == 'L':
                    bit = litter_id[(nr, nc)]
                    nmask |= (1 << bit)

                if classroom[nr][nc] == 'R':
                    ne = energy

                if nmask == full_mask:
                    return moves + 1

                state = (nr, nc, nmask)

                if best.get(state, -1) >= ne:
                    continue

                best[state] = ne
                q.append((nr, nc, ne, nmask, moves + 1))

        return -1