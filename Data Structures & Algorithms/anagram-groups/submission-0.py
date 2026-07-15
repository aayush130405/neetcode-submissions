class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            key = tuple(sorted(i))
            if key not in seen:
                seen[key] = [i]
            else:
                seen[key].append(i)
        return list(seen.values())
