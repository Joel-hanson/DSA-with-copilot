"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

from typing import List


class Solution:
    """
    Algorithm:
        1. Create a variable to store the length of the array, result and prefix
        2. Create a result array with the length of the array
        3. For each number in the array
            a. Set the result at the index to the prefix
            b. Multiply the prefix by the number
        4. Create a variable to store the postfix
        5. For each number in the array in reverse
            a. Multiply the result at the index by the postfix
            b. Multiply the postfix by the number
        6. Return the result
    Pattern: Array
    Time Complexity: O(n) where n is the number of elements in the array
    Space Complexity: O(1)
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length_nums = len(nums)
        res = [1] * length_nums

        prefix = 1
        for i in range(length_nums):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(length_nums - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
