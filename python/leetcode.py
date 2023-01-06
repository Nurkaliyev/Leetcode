from typing import List
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 1. Two Sum
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for index in range(len(nums)):
            if target - nums[index] in num_to_index:
                return [num_to_index[target - nums[index]], index]
            else:
                num_to_index[nums[index]] = index
        return []

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


    # 9. Palindrome Number.md
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False