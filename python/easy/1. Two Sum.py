from typing import List

class Solution:
    # 1. Two Sum
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of the elements
        indices = {}

        # Loop through the list of numbers
        for i, num in enumerate(nums):
            # Check if the target minus the current number is in the dictionary
            if target - num in indices:
                # If it is, return the indices of the pair of numbers
                return [indices[target - num], i]

            # Otherwise, add the current number and its index to the dictionary
            indices[num] = i

        # If we didn't find a pair of numbers, return an empty list
        return []