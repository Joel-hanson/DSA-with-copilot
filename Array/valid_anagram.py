"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


class Solution:
    """
    Algorithm:
        1. Create a dictionary to store the frequency of each character in s
        2. Iterate through each character in t
            a. If the character is not in the dictionary, return False
            b. If the character is in the dictionary, decrement the frequency of the character by 1
            c. If the frequency of the character is 0, remove the character from the dictionary
        3. If the dictionary is not empty, return False
        4. Return True
    Approach: Hash Table
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    def isAnagram(self, s: str, t: str) -> bool:
        frequency = {}

        for char in s:
            frequency[char] = frequency.get(char, 0) + 1

        for char in t:
            char_frequency = frequency.get(char)
            if char_frequency is None:
                return False
            char_frequency -= 1

            if char_frequency == 0:
                del frequency[char]
            else:
                frequency[char] = char_frequency

        if frequency:
            return False
        return True
