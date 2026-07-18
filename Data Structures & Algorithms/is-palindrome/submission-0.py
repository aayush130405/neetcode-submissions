class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_str = s.lower()

        alphanum_str = []

        for i in lower_str:
            if i.isalnum():
                alphanum_str.append(i)

        l = 0
        r = len(alphanum_str) - 1 

        while l <= r:
            if alphanum_str[l] == alphanum_str[r]:
                l += 1
                r -= 1
            else:
                return False

        return True