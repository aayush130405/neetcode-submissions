class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return False
            
            if board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = '#'
            
            found = (
                backtrack(r + 1, c, i + 1) or
                backtrack(r - 1, c, i + 1) or
                backtrack(r, c + 1, i + 1) or
                backtrack(r, c - 1, i + 1)
            )

            board[r][c] = temp
            return found
        
        for m in range(ROWS):
            for n in range(COLS):
                if backtrack(m, n, 0):
                    return True
        
        return False

