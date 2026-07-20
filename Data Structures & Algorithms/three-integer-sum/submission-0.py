class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i > 0:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] == 0:
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right:
                        if nums[left] == nums[left-1]:
                            left += 1
                        else:
                            break

                    while left < right:
                        if nums[right] == nums[right+1]:
                            right -= 1
                        else:
                            break
                else:
                    left += 1

        return answer