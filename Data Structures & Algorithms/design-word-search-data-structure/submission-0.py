class WordDictionary:

    def __init__(self):
        self.dictt = {}

    def addWord(self, word: str) -> None:
        d = self.dictt
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['#'] = '#'

    def search(self, word: str) -> bool:
        def dfs(dictt, i):
            # base case
            if i == len(word):
                return '#' in dictt
            
            ch = word[i]

            # if we have a '.' case:
            if ch == '.':
                for key in dictt:
                    if key != '#' and dfs(dictt[key], i + 1):
                        return True
                return False

            if ch not in dictt:
                return False
            
            return dfs(dictt[ch], i + 1)
        return dfs(self.dictt, 0)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)