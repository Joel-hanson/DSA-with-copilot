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

Answer: Use a dictionary to store the frequency of each character in the first string. Traverse the second string. For each character in the second string, if the character is not in the dictionary, return False. If the character is in the dictionary, decrement the frequency of the character in the dictionary. If the frequency of the character in the dictionary is less than 0, return False. Return True.
"""

from typing import Dict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create a dictionary to store the frequency of each character in the first string
        frequency = {}

        # Traverse the first string
        for character in s:
            # If the character is not in the dictionary
            if character not in frequency:
                # Add the character to the dictionary with a frequency of 1
                frequency[character] = 1

            # If the character is in the dictionary
            else:
                # Increment the frequency of the character in the dictionary
                frequency[character] += 1

        # Traverse the second string
        for character in t:
            # If the character is not in the dictionary
            if character not in frequency:
                # Return False
                return False

            # If the character is in the dictionary
            else:
                # Decrement the frequency of the character in the dictionary
                frequency[character] -= 1

                # If the frequency of the character in the dictionary is less than 0
                if frequency[character] < 0:
                    # Return False
                    return False

        if sum(frequency.values()) != 0:
            return False

        # Return True
        return True


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         frequency_map = {}
#         for char in s:
#             frequency_map[char] = frequency_map.get(char, 0) + 1
#         for char in t:
#             if char in frequency_map:
#                 frequency_map[char] -= 1
#                 if frequency_map[char] < 0:
#                     return False
#             else:
#                 return False
#         for key, value in frequency_map.items():
#             if value != 0:
#                 return False
#         return True


