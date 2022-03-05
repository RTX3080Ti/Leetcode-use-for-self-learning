import random


class Solution:
    # Leetcode 215. Kth Largest Element in an Array
    # Quick Sort
    # N is the size of nums
    # Time Complexity: O(N)
    # Space Complexity: O(logN)
    def findKthLargest(self, nums, k):
        return self.quickSort(nums, 0, len(nums) - 1, k)

    def quickSort(self, nums, left, right, key):
        index = self.randomPartition(nums, left, right)
        if index == key - 1:
            return nums[index]
        else:
            if index > key - 1:
                return self.quickSort(nums, left, index - 1, key)
            else:
                return self.quickSort(nums, index + 1, right, key)

    def randomPartition(self, nums, left, right):
        random_num = random.randint(left, right)
        nums[random_num], nums[right] = nums[right], nums[random_num]
        return self.partition(nums, left, right)

    # 分区函数，将比数组最后一个元素大的元素都放在它的左边，小的都放在它的右边
    def partition(self, nums, left, right):
        pivot = nums[right]
        pivot_index = right
        while left <= right:
            while left <= right and pivot < nums[left]:
                left += 1
            while left <= right and pivot >= nums[right]:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]

        nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
        return left


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 2
s = Solution()
print(s.findKthLargest(nums, k))
