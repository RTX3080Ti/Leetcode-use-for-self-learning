from heapq import heapify, heappush, heappop


class Solution:
    # Leetcode 215. Kth Largest Element in an Array
    # Heap
    # N is the size of nums
    # Time Complexity: O(NlogK)
    # Space Complexity: O(N)
    def findKthLargest(self, nums, k):
        minHeap = []
        heapify(minHeap)
        for num in nums:
            heappush(minHeap, num)
            if len(minHeap) > k:
                heappop(minHeap)
        return minHeap[0]



nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
s = Solution()
print(s.findKthLargest(nums, k))
