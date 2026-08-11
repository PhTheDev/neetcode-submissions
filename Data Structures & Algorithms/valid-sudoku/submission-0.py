class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(len(board)):
            for c in range(len(board)):
                box = (r // 3) * 3 + (c // 3)
                num = board[r][c]
                if num in rows[r]:
                    return False
                if num in cols[c]:
                    return False
                if num in boxes[box]:
                    return False
                if num == ".":
                    continue
                rows[r].add(num)
                cols[c].add(num)
                boxes[box].add(num)
        return True