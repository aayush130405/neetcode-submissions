class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        res = []

        for word in words:
            d = trie
            for c in word:
                if c not in d:
                    d[c] = {}
                d = d[c]
            d['#'] = word

        ROW_NUM, COL_NUM = len(board), len(board[0])

        def dfs(row, col, node):
            if row < 0 or col < 0 or row >= ROW_NUM or col >= COL_NUM:
                return 

            ch = board[row][col]

            if ch not in node:
                return 

            node = node[ch]
            
            if '#' in node:
                res.append(node['#'])
                del node['#']

            board[row][col] = '*'

            dfs(row + 1, col, node)
            dfs(row - 1, col, node)
            dfs(row, col + 1, node)
            dfs(row, col - 1, node)

            board[row][col] = ch
        
        for r in range(ROW_NUM):
            for c in range(COL_NUM):
                dfs(r, c, trie)

        return res