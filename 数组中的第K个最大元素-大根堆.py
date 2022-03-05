class Solution:
    def findKthLargest(self, nums, k):
        n = len(nums)
        self.build_maxHeap(nums)
        # 使用大根堆找出第k大的元素
        for i in range(k - 1):
            nums[0], nums[n - 1 - i] = nums[n - 1 - i], nums[0]
            self.adjust_down(nums, 0, n - 1 - i - 1)
        return nums[0]

    def build_maxHeap(self, nums):
        n = len(nums)
        for root in range(n // 2, -1, -1):
            # 自上而下调整大根堆
            self.adjust_down(nums, root, n - 1)

    def adjust_down(self, nums, root, last):
        if root > last:
            return
        # 保留父亲的值备用于替换
        t = nums[root]
        child = 2 * root + 1
        while child <= last:
            # 选择二叉树中最大的孩子
            if child + 1 <= last and nums[child] < nums[child + 1]:
                child += 1
            if t >= nums[child]:
                break
            # 如果孩子比父亲大，则交换
            nums[root] = nums[child]
            # 继续向下遍历循环上述步骤直到没有孩子
            root = child
            child = 2 * root + 1
        nums[root] = t


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
s = Solution()
print(s.findKthLargest(nums, k))
