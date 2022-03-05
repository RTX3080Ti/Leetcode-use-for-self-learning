class QuickSort:
    def quickSort(self, nums):
        return self.quick_Sort(nums, 0, len(nums) - 1)

    def quick_Sort(self, nums, left, right):
        if left < right:
            pivot = self.partition(nums, left, right)
            self.quick_Sort(nums, left, pivot - 1)
            self.quick_Sort(nums, pivot + 1, right)

        return nums

    # 分区函数，将比数组最后一个元素大的元素都放在它的左边，小的都放在它的右边
    def partition(self, nums, left, right):
        pivot = nums[right]
        pivot_index = right
        while left <= right:
            while left <= right and pivot > nums[left]:
                left += 1
            while left <= right and pivot <= nums[right]:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]

        nums[left], nums[pivot_index] = nums[pivot_index], nums[left]
        return left


nums = [5, 9, 1, 11, 6, 7, 2, 4]
q = QuickSort()
print(q.quickSort(nums))
