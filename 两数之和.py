class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        book = {}
        for i in range(len(nums)):
            if book.get(target - nums[i]) is not None:
                return [book.get(target - nums[i]), i]
            book[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9
s = Solution()

print(s.twoSum(nums, target))
