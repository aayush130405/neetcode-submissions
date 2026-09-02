class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        startingPoint = nums[0]
        fast = startingPoint
        slow = startingPoint

        while fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if fast == slow:
                fast = startingPoint
                while fast != slow:
                    slow = nums[slow]
                    fast = nums[fast]
                return fast