class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        book = {}
        for i in range(len(nums)):
            if nums[i] not in book:
                book[nums[i]] = 1
            else:
                return True
        return False

nums = [1,1]
s = Solution()
print(s.containsDuplicate(nums))