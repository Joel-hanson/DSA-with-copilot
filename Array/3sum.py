"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

Answer: Two Pointers
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Algorithm:
            1. Sort the array
            2. Use a for loop to iterate through the array
            3. Use two pointers to find the triplets
            4. If the sum is less than 0, move the left pointer to the right
            5. If the sum is greater than 0, move the right pointer to the left
            6. If the sum is equal to 0, add the triplets to the result
            7. Return the result
        Pattern: Two Pointers
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Algorithm:
            1. Sort the array
            2. Use a for loop to iterate through the array
            3. Use a hash table to store the frequency of each number
            4. If the number is 0, add the triplets to the result
            5. If the number is greater than 0, break the loop
            6. If the number is not in the hash table, add the triplets to the result
            7. Return the result
        Pattern: Two Pointers
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        nums.sort()
        result = []
        freq = {}
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if nums[i] == 0 and freq.get(nums[i], 0) < 3:
                result.append([0, 0, 0])
            if not freq.get(nums[i]):
                freq[nums[i]] = 1
                left, right = i + 1, len(nums) - 1
                while left < right:
                    if nums[i] + nums[left] + nums[right] < 0:
                        left += 1
                    elif nums[i] + nums[left] + nums[right] > 0:
                        right -= 1
                    else:
                        result.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return result
