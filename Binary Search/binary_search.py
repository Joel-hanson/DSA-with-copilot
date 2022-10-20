"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

Answer: Use binary search to find the target. If the target is found, return the index of the target. If the target is not found, return -1.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Algorithm:
            1. Use binary search to find the target.
            2. If the target is found, return the index of the target.
            3. If the target is not found, return -1.
        Pattern: Binary Search
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # Initialize the left and right indices
        left = 0
        right = len(nums) - 1

        # While the left index is less than or equal to the right index
        # Equal is because if there only one element in the array, the left and right indices will be the same
        while left <= right:
            # Calculate the middle index
            middle = (left + right) // 2

            # If the middle index is equal to the target
            if nums[middle] == target:
                # Return the middle index
                return middle

            # If the middle index is less than the target
            elif nums[middle] < target:
                # Set the left index to the middle index plus 1
                left = middle + 1

            # If the middle index is greater than the target
            else:
                # Set the right index to the middle index minus 1
                right = middle - 1

        # Return -1
        return -1
