class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        start = end = 0
        sum = 0
        min_length = len(nums) + 1
        while end < len(nums):
            sum += nums[end]
            end += 1
            while sum >= target:
                min_length = min(min_length, end - start)
                sum -= nums[start]
                start += 1
        return 0 if min_length == len(nums) + 1 else min_length



target = 7
nums = [2,3,1,2,4,3]
s = Solution()
print(s.minSubArrayLen(target, nums))