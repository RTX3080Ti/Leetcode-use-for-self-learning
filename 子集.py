class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        res.append([])
        path = []
        used = []
        def backtrack(nums, start):
            if len(path) > 0:
                res.append(path[:])
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                path.append(nums[i])
                used.append(nums[i])
                backtrack(nums, i+1)
                used.pop()
                path.pop()
        backtrack(nums, 0)
        return res

nums = [1,2,2]
s = Solution()
print(s.subsets(nums))
