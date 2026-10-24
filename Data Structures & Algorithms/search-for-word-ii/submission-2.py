class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie = {}
        res = []
        for word in words:
            d = trie
            for c in word:
                if c not in d:
                    d[c] = {}
                d = d[c]
            d['#'] = word

        rows, cols = len(board), len(board[0]) # define rows and cols

        def dfs(row, col, node):
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return 
            
            ch = board[row][col]
            if ch not in node:
                return 
            
            node = node[ch]
            if '#' in node:
                res.append(node['#'])
                del node['#']
            
            board[row][col] = '*' # Mark the current cell as visited

            dfs(row - 1, col, node)
            dfs(row + 1, col, node)
            dfs(row, col - 1, node)
            dfs(row, col + 1, node)

            board[row][col] = ch # Restore the cell (backtracking)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)

        return res