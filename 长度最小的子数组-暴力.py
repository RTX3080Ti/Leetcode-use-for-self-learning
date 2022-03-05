class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_length = len(nums) + 1

        for i in range(0, len(nums)):
            sum = 0
            sum += nums[i]
            if sum >= target:
                return 1
            for j in range(i+1, len(nums)):
                sum += nums[j]
                if sum >= target:
                    length = j - i + 1
                    if min_length > length:
                        min_length = length
                        break

        return 0 if min_length == len(nums) + 1 else min_length

target = 1
nums = [2,3,1,2,4,3]
s = Solution()
print(s.minSubArrayLen(target, nums))