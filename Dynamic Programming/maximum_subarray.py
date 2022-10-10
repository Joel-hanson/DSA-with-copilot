"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.


Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Answer: Use dynamic programming to find the maximum subarray. The maximum subarray at index i is the maximum of the maximum subarray at index i minus 1 plus the current element or the current element. The maximum subarray is the maximum of the maximum subarray at each index.
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Initialize the maximum subarray at index 0
        maximum_subarray = nums[0]

        # Initialize the maximum subarray at index 0
        maximum_subarray_at_index = nums[0]

        # Traverse the array from index 1 to the end of the array
        for index in range(1, len(nums)):
            # Calculate the maximum subarray at index i
            maximum_subarray_at_index = max(
                maximum_subarray_at_index + nums[index], nums[index]
            )

            # Calculate the maximum subarray
            maximum_subarray = max(maximum_subarray, maximum_subarray_at_index)

        # Return the maximum subarray
        return maximum_subarray


# Divide and Conquer Approach
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n log n)
        Space Complexity: O(log n)
        """
        # Return the maximum subarray
        return self.divide_and_conquer(nums, 0, len(nums) - 1)

    def divide_and_conquer(self, nums: List[int], left: int, right: int) -> int:
        # If the left index is greater than the right index
        if left > right:
            # Return the minimum integer
            return -float("inf")

        # Calculate the middle index
        middle = (left + right) // 2

        # Calculate the maximum subarray at the middle index
        maximum_subarray_at_middle = nums[middle]

        # Calculate the maximum subarray at the middle index
        maximum_subarray_at_middle_left = nums[middle]

        # Calculate the maximum subarray at the middle index
        maximum_subarray_at_middle_right = nums[middle]

        # Calculate the maximum subarray at the middle index
        for index in range(middle - 1, left - 1, -1):
            # Calculate the maximum subarray at the middle index
            maximum_subarray_at_middle_left += nums[index]

            # Calculate the maximum subarray at the middle index
            maximum_subarray_at_middle = max(
                maximum_subarray_at_middle, maximum_subarray_at_middle_left
            )

        # Calculate the maximum subarray at the middle index
        for index in range(middle + 1, right + 1):
            # Calculate the maximum subarray at the middle index
            maximum_subarray_at_middle_right += nums[index]

            # Calculate the maximum subarray at the middle index
            maximum_subarray_at_middle = max(
                maximum_subarray_at_middle, maximum_subarray_at_middle_right
            )

        # Calculate the maximum subarray at the middle index
        maximum_subarray_at_middle = max(
            maximum_subarray_at_middle,
            maximum_subarray_at_middle_left
            + maximum_subarray_at_middle_right
            - nums[middle],
        )

        # Calculate the maximum subarray at the left index
        maximum_subarray_at_left = self.divide_and_conquer(nums, left, middle - 1)

        # Calculate the maximum subarray at the right index
        maximum_subarray_at_right = self.divide_and_conquer(nums, middle + 1, right)

        # Return the maximum subarray
        return max(
            maximum_subarray_at_middle,
            maximum_subarray_at_left,
            maximum_subarray_at_right,
        )


if __name__ == "__main__":
    # Initialize the solution
    solution = Solution()

    # Print the solution
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    # Print the solution
    print(solution.maxSubArray([1]))

    # Print the solution
    print(solution.maxSubArray([5, 4, -1, 7, 8]))

    # Print the solution
    print(solution.maxSubArray([-2, 1]))

    # Print the solution
    print(solution.maxSubArray([-2, -1]))

    # Print the solution
    print(solution.maxSubArray([-1, -2]))

    # Print the solution
    print(solution.maxSubArray([-1, 0]))

    # Print the solution
    print(solution.maxSubArray([-2, 1]))

    # Print the solution
    print(solution.maxSubArray([-2, 1, 3]))

    # Print the solution
    print(solution.maxSubArray([-2, 1, 3, 4]))

    # Print the solution
    print(solution.maxSubArray([-2, 1, 3, 4, 5]))

    # Print the solution
    print(solution.maxSubArray([-2, 1, 3, 4, 5, 6]))

    # Print the solution
    print(solution.maxSubArray([-2, 1, 3, 4, 5, 6, 7]))

    # Print the solution
    print(solution.maxSubArray([-2, 1, 3, 4, 5, 6, 7, 8]))

    # Print the solution
    print(solution.maxSubArray([-2, 1, 3, 4, 5, 6, 7, 8, 9]))

    # Print the solution
    print(solution.maxSubArray([-2, 1, 3, 4, 5, 6, 7, 8, 9, 10]))

    # Print the solution
    print(solution.maxSubArray([-2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11]))

    # Print the solution
    print(solution.maxSubArray([-2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

    # Print the solution
    print(solution.maxSubArray([-2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
