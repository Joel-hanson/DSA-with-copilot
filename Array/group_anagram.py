"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from typing import List


class Solution:
    """
    Algorithm:
        1. Create a dictionary to store the anagrams
        2. For each string in the array
            a. Create a variable to store the count of each character
            b. For each character in the string
                i. Increment the count of the character
            c. Add the string to the dictionary with the count as the key
        3. Return the values of the dictionary
    Pattern: Hash Table
    Time Complexity: O(n * m) where n is the number of strings and m is the length of the longest string
    Space Complexity: O(n * m)
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for string in strs:
            count = [0] * 26

            for char in string:
                count[ord(char) - ord("a")] += 1
            res[tuple(count)] = res.get(tuple(count), []) + [string]

        return list(res.values())
