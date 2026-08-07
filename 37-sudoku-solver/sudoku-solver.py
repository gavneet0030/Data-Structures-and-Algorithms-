class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Initialize sets
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + (j // 3)].add(num)

        def backtrack(idx):
            if idx == len(empty):
                return True

            r, c = empty[idx]
            box = (r // 3) * 3 + (c // 3)

            for ch in "123456789":
                if (
                    ch not in rows[r]
                    and ch not in cols[c]
                    and ch not in boxes[box]
                ):
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[box].add(ch)

                    if backtrack(idx + 1):
                        return True

                    board[r][c] = "."
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[box].remove(ch)

            return False

        backtrack(0)