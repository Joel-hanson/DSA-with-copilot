"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Answer: Sliding Window
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Algorithm:
            1. Use a sliding window to find the longest substring without repeating characters
            2. Use a hash table to store the frequency of each character in the sliding window
            3. If the character is in the hash table and the frequency is greater than 0, move the left pointer to the right until the character is no longer in the hash table
            4. Update the hash table and the max length
            5. Return the max length
        Pattern: Sliding Window
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        left, right = 0, 0
        max_length = 0
        freq = {}
        while right < len(s):
            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1
            while freq[s[right]] > 1:
                freq[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Algorithm:
            1. Use a sliding window to find the longest substring without repeating characters
            2. Use a hash table to store the index of each character in the sliding window
            3. If the character is in the hash table and the index is greater than or equal to the left pointer, move the left pointer to the right of the index
            4. Update the hash table and the max length
            5. Return the max length
        Pattern: Sliding Window
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        left = 0
        charSet = set()
        res = 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            res = max(res, right - left + 1)
        return res


"""
aadfwdca

left = 0
right = 0
max_length = 0
freq = {}

right = 0
freq = {a: 1}
max_length = 1

right = 1
left = 0
freq = {a: 2}
max_length = 1
left = 1
freq = {a: 1}
max_length = 1

right = 2
freq = {a: 1, d: 1}
max_length = 2

right = 3
freq = {a: 1, d: 1, f: 1}
max_length = 3

right = 4
freq = {a: 1, d: 1, f: 1, w: 1}
max_length = 4

right = 5
freq = {a: 1, d: 2, f: 1, w: 1}
max_length = 4
left = 1
freq = {a: 0, d: 2, f: 1, w: 1}
max_length = 4
left = 2
freq = {a: 0, d: 1, f: 1, w: 1}
max_length = 4

right = 6
freq = {a: 0, d: 1, f: 1, w: 1, c: 1}
max_length = 4

right = 7
freq = {a: 1, d: 1, f: 1, w: 1, c: 1}
max_length = 5

"""
