class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        longest = 0

        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]] += 1
            
            rep_req = (r - l + 1) - max(freq.values())

            if rep_req <= k:
               longest = max(longest, r - l + 1)
            else:
                while rep_req > k:
                    freq[s[l]] -= 1
                    l += 1
                    rep_req = (r - l + 1) - max(freq.values())
                longest = max(longest, r - l + 1)
                
        
        return longest
             