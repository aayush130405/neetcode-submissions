class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        freq = {}
        max_freq = 0

        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 1
                max_freq = max(max_freq, freq[s[r]])
            else:
                freq[s[r]] += 1
                max_freq = max(max_freq, freq[s[r]])
            
            rep_req = (r - l + 1) - max_freq

            while rep_req > k:
                freq[s[l]] -= 1
                l += 1
                rep_req = (r - l + 1) - max_freq 
            longest = max(longest, r - l + 1)
        return longest