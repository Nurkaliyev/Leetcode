from typing import List
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 1. Two Sum
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of the elements
        indices = {}

        # Loop through the list of numbers
        for index, num in enumerate(nums):
            # Check if the target minus the current number is in the dictionary
            if target - num in indices:
                # If it is, return the indices of the pair of numbers
                return [indices[target - num], index]
            else:
                # Otherwise, add the current number and its index to the dictionary
                indices[num] = index

        # If we didn't find a pair of numbers, return an empty list
        return []

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
            sum = x + y + carry
            carry = sum // 10
            current.next = ListNode(sum % 10)
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

    # 3. Longest Substring Without Repeating Characters
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set to store characters in current substring
        char_set = set()
        # initialize max length
        max_len = 0
        # initialize start and end pointers
        start = 0
        end = 0
        # loop until end pointer reaches end of string
        while end < len(s):
            # if current character not in char_set
            if s[end] not in char_set:
                # add current character to char_set and update max_len if necessary
                char_set.add(s[end])
                end += 1
                max_len = max(max_len, end - start)
            else:
                # if current character is already in char_set, remove characters from start until current character is removed
                char_set.remove(s[start])
                start += 1
        # return max length
        return max_len


    # 9. Palindrome Number
    def isPalindrome(self, x: int) -> bool:
        # Special case: negative numbers are not palindromes
        if x < 0:
            return False

        # Convert the number to a string and check if the string is the same forwards and backwards
        return str(x) == str(x)[::-1]