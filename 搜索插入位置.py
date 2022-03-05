class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid

        return left if nums[left] >= target else left + 1

s = Solution()
nums = [0, 1, 3, 5]
target = 4
print(s.searchInsert(nums, target))

