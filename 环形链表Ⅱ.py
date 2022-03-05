from LinkList import *

class Solution:
    # def hasCycle(self, head: ListNode) -> bool:
    #     fast = slow = head
    #     while fast != None and slow != None:
    #         slow = slow.next
    #         fast = fast.next
    #         if fast != None:
    #             fast = fast.next
    #         else:
    #             return False
    #         if fast == slow:
    #             return True
    #     return False

    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while True:
            if not fast and not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow

head = [1]
head = build_ListNode(head) if head != [] else None
# tail = find_tail(head)
cur = head

pos = -1
if pos >0:
    while pos > 0:
        cur = cur.next
        pos -= 1

elif pos == 0:
    cur = head

else:
    cur = None

# tail.next = cur

s = Solution()
print(s.detectCycle(head))