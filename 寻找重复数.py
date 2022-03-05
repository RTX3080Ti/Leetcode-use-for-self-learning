class Solution:
    def findDuplicate(self, nums) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast

class Solution1:
    def findDuplicate(self, nums) -> int:
        right = len(nums) - 1
        left = 1
        while left < right:
            mid = left + (right - left) // 2
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1

            if cnt > mid:
                right = mid
            else:
                left = mid + 1

        return left



nums = [3,1,1,4,2]
s = Solution1()
print(s.findDuplicate(nums))
