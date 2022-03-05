class Solution:
    def missingNumber(self, nums) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

class Solution2:
    def missingNumber(self, nums) -> int:
        s = set(nums)
        for i in range(len(nums) + 1):
            if i not in s:
                return i

class Solution3:
    def missingNumber(self, nums) -> int:
        xor = 0
        for i, num in enumerate(nums):
            xor ^= i ^ num
        return xor ^ len(nums)

nums = [8,6,4,2,3,5,7,0,1]
s = Solution3()
print(s.missingNumber(nums))