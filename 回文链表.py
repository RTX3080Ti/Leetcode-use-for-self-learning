# Definition for singly-linked list.
import LinkList
from LinkList import  *

class Solution(object):
    def isPalindrome(self, head: ListNode) -> bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        '''
        # 数组
        for i in range(len(head) // 2):
            if head[i] != head[len(head) - 1 - i]:
                return False
        return True
        '''

        '''
        # 递归
        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()
        '''

        '''
        # 将链表存进数组
        cur = head
        nums = []
        while cur != None:
            nums.append(cur.val)
            cur = cur.next
        return nums == nums[::-1]
        '''
        half_list = self.fast_slow_cur(head)
        reversed_half_list = self.reverseList(half_list.next)
        half_list.next = reversed_half_list

        first_point = head
        second_point = reversed_half_list
        while second_point != None:
            if first_point.val != second_point.val:
                return False
            first_point = first_point.next
            second_point = second_point.next

        half_list.next = self.reverseList(reversed_half_list)
        return True


    # 快慢指针，可将慢指针移动至链表中间位置
    def fast_slow_cur(self, head: ListNode):
        fast = slow = head
        while fast.next != None and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # 反转后半段链表
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur != None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


head = [2,7,3,4,3,7,2]
head = build_ListNode(head)
# print_ListNode(head, 'SINGLE')
s = Solution()
print(s.isPalindrome(head))