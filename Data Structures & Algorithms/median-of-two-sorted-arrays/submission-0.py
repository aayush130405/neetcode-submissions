class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(a) > len(b):
            a, b = b, a

        left = 0
        right = len(a) 

        while left <= right:
            mid = (left + right) // 2

            elements_in_left = (len(a) + len(b)) // 2

            mid_of_b = elements_in_left - mid

            if mid > 0:
                a_left = a[mid - 1]
            else:
                a_left = float("-inf")

            if mid < len(a):
                a_right = a[mid]
            else:
                a_right = float("inf")

            if mid_of_b > 0:    
                b_left = b[mid_of_b - 1]
            else:
                b_left = float("-inf")
            
            if mid_of_b < len(b):
                b_right = b[mid_of_b]
            else:
                b_right = float("inf")


            if a_left > b_right:
                right = mid - 1
            elif b_left > a_right:
                left = mid + 1
            else:
                if (len(a) + len(b)) % 2 != 0:
                    median = min(a_right, b_right)
                else:
                    median = (max(a_left, b_left) + min(a_right, b_right)) / 2
                return median