class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['#'] = '#'

    def search(self, word: str) -> bool:
        def dfs(trie, i):
            if i == len(word):
                return '#' in trie
            
            ch = word[i]

            if ch == '.':
                for key in trie:
                    if key != '#' and dfs(trie[key], i + 1):
                        return True
                    # return False

            if ch not in trie:
                return False
            
            return dfs(trie[ch], i + 1)
        return dfs(self.trie, 0)
