class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

# 将数组转换为链表
def build_ListNode(nums):
    head = ListNode(nums[0])
    cur = head
    for i in nums[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return head

# 打印不同格式的链表
def print_ListNode(head, p_type="SINGLE"):
    p = head
    result = []
    while p:
        if p_type in ["STR", "SINGLE"]:
            result.append(str(p.val))
        else:
            result.append(p.val)
        p = p.next
    if p_type == "STR":
        print(" ".join(result))
    elif p_type == "LIST":
        print(result)
    elif p_type == "SINGLE":
        print(" -> ".join(result))
    else:
        print("error dType!!!")

def find_tail(head):
    tail = head
    while tail.next != None:
        tail = tail.next

    return tail


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 8, 1, 2]
    head = build_ListNode(nums)
    print_ListNode(head, "SINGLE")