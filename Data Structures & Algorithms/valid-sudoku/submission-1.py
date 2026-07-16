class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        boxes = {}
        for row in range(9):
            for col in range(9):
                box_id = (row//3, col//3)
                if box_id not in boxes:
                    boxes[box_id] = set()
                if board[row][col] == ".":
                    continue
                if board[row][col] in boxes[box_id]:
                    return False
                boxes[box_id].add(board[row][col])

        return True