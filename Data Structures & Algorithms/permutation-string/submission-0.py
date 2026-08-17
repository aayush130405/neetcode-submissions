class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        window_freq = {}
        l = 0
        
        for i in s1:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
            
        for r in range(len(s2)):
            if s2[r] not in window_freq:
                window_freq[s2[r]] = 1
            else:
                window_freq[s2[r]] += 1
            
            if r - l + 1 == len(s1):
                if window_freq == freq:
                    return True
                window_freq[s2[l]] -= 1
                if window_freq[s2[l]] == 0:
                    del window_freq[s2[l]]
                l += 1
        return False