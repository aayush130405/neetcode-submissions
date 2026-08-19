class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        win_map = {}
        
        l = 0

        for i in s1:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        for r in range(len(s2)):
            if s2[r] not in win_map:
                win_map[s2[r]] = 1
            else:
                win_map[s2[r]] += 1
            
            if r - l + 1 == len(s1):
                if win_map == freq:
                    return True
                win_map[s2[l]] -= 1
                if win_map[s2[l]] == 0:
                    del win_map[s2[l]]
                l += 1
        return False
            