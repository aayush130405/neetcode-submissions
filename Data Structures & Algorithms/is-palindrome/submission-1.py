class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowered = s.lower()
        alnum_str = []

        for i in lowered:
            if i.isalnum():
                alnum_str.append(i)

        left = 0
        right = len(alnum_str) - 1

        while left < right:
            if alnum_str[left] == alnum_str[right]:
                left += 1
                right -= 1
            else:
                return False

        return True
