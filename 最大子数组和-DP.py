class Solution:
    def maxSubArray(self, nums) -> int:
        temp = []
        temp.append(nums[0])
        maxSum = nums[0]
        for i in range(1, len(nums)):
            if temp[i - 1] > 0:
                ans = nums[i] + temp[i - 1]
                temp.append(ans)
            else:
                ans = nums[i]
                temp.append(ans)
            if maxSum < ans:
                maxSum = ans

        return maxSum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
num = [1]
s = Solution()
print(s.maxSubArray(num))