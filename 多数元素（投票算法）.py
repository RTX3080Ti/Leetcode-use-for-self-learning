class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = nums[0]
        cnt = 1
        if len(nums) == 1:
            return nums[0]
        for i in range(1, len(nums)):
            if nums[i] == num:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    cnt = 1
                    num = nums[i]
        return num

s = Solution()
print(s.majorityElement(nums=[2147483647]))