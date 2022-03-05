class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.getMax(nums, 0, len(nums)-1)

    def getMidMax(self, nums, left, right):
        mid = left + (right - left) // 2
        leftSum = nums[mid]
        leftMax = leftSum
        for i in range(mid-1, left-1, -1):
            leftSum += nums[i]
            leftMax = max(leftSum, leftMax)
        rightSum = nums[mid+1]
        rightMax = rightSum
        for j in range(mid+2, right+1):
            rightSum += nums[j]
            rightMax = max(rightSum, rightMax)
        return leftMax + rightMax

    def getMax(self, nums, left, right):
        if left == right:
            return nums[left]
        mid = left + (right - left) // 2
        leftMax = self.getMax(nums, left, mid)
        rightMax = self.getMax(nums, mid+1, right)
        midMax = self.getMidMax(nums, left, right)

        return max(leftMax, rightMax, midMax)

nums = [5,4,-1,7,8]
s = Solution()
print(s.maxSubArray(nums))



            