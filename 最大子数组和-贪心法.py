class Solution:
    def maxSubArray(self, nums) -> int:
        ans = nums[0]
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum > ans:
                ans = sum
            if sum < 0:
                sum = 0
        return ans


nums = [5, 4, -1, 7, 8]
s = Solution()
print(s.maxSubArray(nums))
