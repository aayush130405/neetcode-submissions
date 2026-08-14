class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        if len(a) > len(b):
            a,b=b,a

        l = 0
        r = len(a) 

        while l <= r:
            m = (l + r) // 2

            on_left = (len(a) + len(b)) // 2

            m_b = on_left - m

            if m > 0:
                a_left = a[m - 1]
            else:
                a_left = float("-inf")
            
            if m_b > 0:
                b_left = b[m_b - 1]
            else:
                b_left = float("-inf") 
                
            if m < len(a):
                a_right = a[m]
            else:
                a_right = float("inf")
            
            if m_b < len(b):
                b_right = b[m_b]
            else:
                b_right = float("inf")

            if a_left > b_right:
                r = m - 1
            elif b_left > a_right:
                l = m + 1
            else:
                if (len(a) + len(b)) % 2 != 0:
                    return min(b_right, a_right)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2