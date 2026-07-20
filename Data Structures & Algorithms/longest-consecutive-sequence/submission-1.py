class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        longest = 0

        for i in nums:
            seen.add(i)

        for i in seen:
            if i-1 in seen:
                continue
            else:
                length = 1
                current = i

                while current + 1 in seen:
                    length += 1
                    current += 1
                longest = max(length, longest)

        return longest