from typing import List

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