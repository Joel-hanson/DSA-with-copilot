"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

Answer: Use two pointers, one at the beginning of the string and one at the end of the string. Move the pointers towards each other, comparing the characters at each pointer. If the characters are not equal, return False. If the pointers meet, return True.
"""


class Solution:
    def isPalindrome(self, string: str) -> bool:
        """
        Algorithm:
            1. Use two pointers, one at the beginning of the string and one at the end of the string.
            2. Move the pointers towards each other, comparing the characters at each pointer.
            3. If the characters are not equal, return False.
            4. If the pointers meet, return True.
        Pattern: Two Pointers
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Create a variable to store the left pointer
        left_pointer = 0

        # Create a variable to store the right pointer
        right_pointer = len(string) - 1

        # While the left pointer is less than or equal to the right pointer
        while left_pointer <= right_pointer:
            # If the character at the left pointer is not alphanumeric
            if not string[left_pointer].isalnum():
                # Move the left pointer to the next character
                left_pointer += 1

            # If the character at the right pointer is not alphanumeric
            elif not string[right_pointer].isalnum():
                # Move the right pointer to the previous character
                right_pointer -= 1

            # If the character at the left pointer is alphanumeric and the character at the right pointer is alphanumeric
            else:
                # If the character at the left pointer is not equal to the character at the right pointer
                if string[left_pointer].lower() != string[right_pointer].lower():
                    # Return False
                    return False

                # Move the left pointer to the next character
                left_pointer += 1

                # Move the right pointer to the previous character
                right_pointer -= 1

        # Return True
        return True
