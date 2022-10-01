"""
https://leetcode.com/problems/valid-parentheses/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

Answer: Use a stack to store the opening brackets. For each closing bracket, check if the stack is empty. If it is, return False. If not, pop the top element from the stack and check if it is the corresponding opening bracket. If it is, continue. If not, return False. If the stack is empty at the end, return True. If not, return False.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # Create a stack to store the opening brackets
        stack = []

        # For each character in the string
        for c in s:
            # If it is an opening bracket
            if c in "([{":
                # Push it to the stack
                stack.append(c)

            # If it is a closing bracket
            else:
                # Check if the stack is empty
                if len(stack) == 0:
                    # If it is, return False
                    return False

                # Pop the top element from the stack
                top = stack.pop()

                # Check if it is the corresponding opening bracket
                if c == ")" and top != "(":
                    return False
                if c == "]" and top != "[":
                    return False
                if c == "}" and top != "{":
                    return False

        # If the stack is empty at the end, return True
        if len(stack) == 0:
            return True

        # If not, return False
        return False
