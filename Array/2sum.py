"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?

Answer: Yes, use a hash table to store the values and their indices. Then, for each value, check if the target minus the value is in the hash table. If it is, return the indices of the value and the target minus the value. If not, add the value and its index to the hash table.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hash table to store the values and their indices
        hash_table = {}

        # For each value in the array
        for i, value in enumerate(nums):
            diff_value = target - value
            # Check if the target minus the value is in the hash table
            diff_index = hash_table.get(diff_value)
            if diff_index is not None:

                # If it is, return the indices of the value and the target minus the value
                return [diff_index, i]

            # If not, add the value and its index to the hash table
            hash_table[value] = i
