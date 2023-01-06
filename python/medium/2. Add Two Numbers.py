from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 2. Add Two Numbers
    def addTwoNumbers(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Initialize variables to store the result and carry value
        result = ListNode(0)
        current = result
        carry = 0

        # Loop through both lists until they are both empty
        while list1 is not None or list2 is not None:
            # Get the values of the current nodes, or use 0 if the node is None
            x = list1.val if list1 is not None else 0
            y = list2.val if list2 is not None else 0

            # Calculate the sum and carry value
            s = x + y + carry
            carry = s // 10
            current.next = ListNode(s % 10)
            current = current.next

            # Move to the next nodes in the lists
            if list1 is not None:
                list1 = list1.next
            if list2 is not None:
                list2 = list2.next

        # If there is a carry value left over, add it to the result
        if carry > 0:
            current.next = ListNode(carry)

        # Return the result, skipping the initial placeholder node
        return result.next