"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

from typing import List


class Solution:
    """
    Algorithm:
        1. Create a set of the numbers
        2. Create a variable to store the result
        3. For each number in the set
            a. If the number - 1 is not in the set
                i. Create a variable to store the current number
                ii. Create a variable to store the current length
                iii. While the current number is in the set
                    1. Increment the current length
                    2. Increment the current number
                iv. Set the result to the max of the result and the current length
        4. Return the result
    Pattern: Array
    Time Complexity: O(n) where n is the number of elements in the array
    Space Complexity: O(n)
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                while current_num + 1 in num_set:
                    current_length += 1
                    current_num += 1
                result = max(result, current_length)
        return result
