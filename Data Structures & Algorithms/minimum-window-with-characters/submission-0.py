class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minn = float("inf")
        cond = 0
        l = 0

        best_left = 0
        best_right = len(s)

        freq = {}
        win_map = {}

        for i in t:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        cond = len(freq)

        for r in range(len(s)):
            if s[r] not in win_map:
                win_map[s[r]] = 1
                if s[r] in freq and freq[s[r]] == win_map[s[r]]:
                    cond -= 1
            else:
                win_map[s[r]] += 1
                if s[r] in freq and freq[s[r]] == win_map[s[r]]:
                    cond -= 1
            
            while cond == 0:
                if r - l + 1 < minn:
                    minn = r - l + 1
                    best_left = l 
                    best_right = r
                win_map[s[l]] -= 1
                if s[l]in freq and win_map[s[l]] < freq[s[l]]:
                    cond += 1
                l += 1
        
        if minn == float("inf"):
            return ""
        else:
            return s[best_left:best_right + 1]