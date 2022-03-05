class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        path = []
        used = []
        def backtrack(nums, used):
            if len(path) == len(nums):
                res.append(path[:])
            for i in range(len(nums)):
                if nums[i] in used:
                    continue
                path.append(nums[i])
                used.append(nums[i])
                backtrack(nums,used)
                used.pop()
                path.pop()
        backtrack(nums, used)
        return res


nums = [1, 2, 3]
s = Solution()
print(s.permute(nums))