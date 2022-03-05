class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        queue = []
        sum = 0
        n = 0
        i = 0
        min_length = len(nums) + 1
        while n < len(nums):
            sum += nums[n]
            queue.append(nums[n])
            n += 1
            while sum >= target:
                min_length = min(min_length, n-i)
                sum -= nums[i]
                i += 1
        return 0 if min_length == len(nums) + 1 else min_length


target = 7
nums = [2,3,1,2,4,3]
s = Solution()
print(s.minSubArrayLen(target, nums))