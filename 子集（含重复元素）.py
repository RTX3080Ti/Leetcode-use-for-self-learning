class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        res.append([])
        path = []
        used = [0] * len(nums)
        def backtrack(nums, start):
            if len(path) > 0 and path not in res:
                res.append(path[:])
            for i in range(start, len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = 1
                backtrack(nums, i+1)
                used[i] = 0
                path.pop()
        backtrack(nums, 0)
        return res

nums = [4,4,4,1,4]
nums = sorted(nums)
s = Solution()
print(s.subsetsWithDup(nums))
