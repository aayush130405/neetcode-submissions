class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = s.lower()
        alnum = []

        for i in low:
            if i.isalnum():
                alnum.append(i)

        left = 0
        right = len(alnum) - 1

        while left < right:
            if alnum[left] == alnum[right]:
                left += 1
                right -= 1
            else:
                return False

        return True
            