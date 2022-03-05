class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        l = 0
        r = len(nums) - 1
        while l < r:
            while(l < r and nums[l] != val):
                l += 1
            while(l < r and nums[r] == val):
                r -= 1
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp

        return l if nums[l] == val else l + 1

s = Solution()
nums = [0, 2, 3, 7 ,6, 4, 3, 4]
val = 2
print(s.removeElement(nums, val))