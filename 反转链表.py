# Definition for singly-linked list.
from LinkList import *
# 迭代
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur != None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

# 递归
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        cur = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return cur


head = [1, 2, 3, 4, 5, 8, 1, 2]
head = build_ListNode(head)
s = Solution()
print_ListNode(s.reverseList(head), 'SINGLE')
