class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start = nums[0]
        slow = start
        fast = start

        while fast:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                fast = start
                while fast != slow:
                    fast = nums[fast]
                    slow = nums[slow]
                return fast