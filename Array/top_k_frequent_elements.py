"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from typing import List


class Solution:
    """
    Algorithm:
        1. Create a dictionary to store the frequency of each number
        2. Create a dictionary to store the numbers with the same frequency
        3. For each number in the array
            a. Increment the frequency of the number
        4. For each number in the dictionary
            a. Add the number to the dictionary with the frequency as the key
        5. Create a variable to store the result
        6. For each frequency in the dictionary
            a. For each number in the dictionary
                i. Add the number to the result
                ii. If the length of the result is equal to k, return the result
        7. Return the result
    Pattern: Hash Table
    Time Complexity: O(n) where n is the number of elements in the array
    Space Complexity: O(n)
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq_map = {}
        freq_to_num_map = {}
        for num in nums:
            num_to_freq_map[num] = num_to_freq_map.get(num, 0) + 1

        for num, freq in num_to_freq_map.items():
            freq_to_num_map[freq] = freq_to_num_map.get(freq, []) + [num]

        result = []
        for i in range(len(nums), -1, -1):
            if i in freq_to_num_map:
                for res in freq_to_num_map[i]:
                    result.append(res)
                    if len(result) == k:
                        return result
        return []
