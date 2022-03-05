from LinkList import *

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        while fast != None and slow != None:
            slow = slow.next
            fast = fast.next
            if fast != None:
                fast = fast.next
            else:
                return False
            if fast == slow:
                return True
        return False

head = [1]
head = build_ListNode(head)
tail = find_tail(head)
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

tail.next = cur

s = Solution()
print(s.hasCycle(head))