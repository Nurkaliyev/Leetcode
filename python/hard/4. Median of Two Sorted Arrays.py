from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the two input arrays into one sorted list
        merge_list = sorted(nums1 + nums2)

        # Compute the length of the merged list
        n = len(merge_list)

        # Compute the median depending on whether n is even or odd
        if n % 2 == 0:
            # If n is even, the median is the average of the middle two elements
            middle_right = n // 2
            middle_left = middle_right - 1
            median = (merge_list[middle_left] + merge_list[middle_right]) / 2
        else:
            # If n is odd, the median is the middle element
            middle = n // 2
            median = merge_list[middle]

        return median