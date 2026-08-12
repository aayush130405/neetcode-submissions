class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(a) > len(b):
            a, b = b, a

        l = 0
        r = len(a)

        while l <= r:
            mid_a = (l + r) // 2

            nums_in_left = (len(a) + len(b)) // 2

            mid_b = nums_in_left - mid_a
            
            if mid_a > 0:
                a_left = a[mid_a - 1]
            else:
                a_left = float("-inf")

            if mid_a < len(a):
                a_right = a[mid_a]
            else:
                a_right = float("inf")
            
            if mid_b > 0:
                b_left = b[mid_b - 1]
            else:
                b_left = float("-inf")

            if mid_b < len(b):
                b_right = b[mid_b]
            else:
                b_right = float("inf")
            

            if a_left > b_right:
                r = mid_a - 1
            elif b_left > a_right:
                l = mid_a + 1
            else:
                if (len(a) + len(b)) % 2 != 0:
                    return min(a_right, b_right)
                else:
                    return (max(a_left,b_left)+min(a_right,b_right))/2
