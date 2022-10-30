'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.


Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.

Answer: Hash Table
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Algorithm:
            1. Use a hash table to store the frequency of each character in magazine
            2. Iterate through ransomNote and check if the character is in the hash table and the frequency is greater than 0
        Pattern: Hash Table
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        freq = {}
        for char in magazine:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        for char in ransomNote:
            if char in freq and freq[char] > 0:
                freq[char] -= 1
            else:
                return False
        return True

