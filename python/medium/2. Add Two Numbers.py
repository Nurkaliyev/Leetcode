from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 2. Add Two Numbers
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        node = head
        reminder = 0
        while l1 or l2 or reminder:
            if l1:
                reminder += l1.val
                l1 = l1.next
            if l2:
                reminder += l2.val
                l2 = l2.next
            node.next = ListNode(reminder % 10)
            reminder //= 10
            node = node.next

        return head.next

