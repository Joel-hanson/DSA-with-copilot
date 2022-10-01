"""
> For a sliding window problem first thing we should do is to create a map to store the frequency of each character in the pattern.
a - 1
b - 1
c - 1
> Then we will have two pointers, one pointer for the beginning of the window and one pointer for the end of the window.
t1 = 0
t2 = 0
> We should have the count variable to keep track of the number of characters matched in the current window.
count = len(pattern)
> We should have the left and right index variables to keep track of the minimum window.
left = 0
right = len(string)
> We should havethe minimum length variable to keep track of the minimum length of the window because the minimum length of the window will less than or equal to the length of the string.
min_length = len(string)
> A variable to know if the minimum window is found or not.
found = False
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len_of_t = len(t)
        len_of_s = len(s)
        if len_of_t > len_of_s:
            return ""
        if t == s:
            return s
        if len_of_t == 0:
            return ""
        pattern_map = self.get_pattern_map(t)
        t1 = 0
        t2 = 0
        count = len_of_t
        left = 0
        right = len_of_s
        min_length = len_of_s
        found = False
        while t2 < len_of_s:
            count = self.handle_pattern_count(s, pattern_map, t2, count)
            while count == 0:
                found = True
                if t2 - t1 + 1 < min_length:
                    min_length = t2 - t1 + 1
                    left = t1
                    right = t2
                if s[t1] in pattern_map:
                    pattern_map[s[t1]] += 1
                    if pattern_map[s[t1]] > 0:
                        count += 1
                t1 += 1
            t2 += 1
        if found:
            return s[left : right + 1]
        return ""

    def handle_pattern_count(self, s, pattern_map, t2, count):
        if s[t2] in pattern_map:
            if pattern_map[s[t2]] > 0:
                count -= 1
            pattern_map[s[t2]] -= 1
        return count

    def get_pattern_map(self, pattern):
        pattern_map = {}
        for char in pattern:
            if char not in pattern_map:
                pattern_map[char] = 0
            pattern_map[char] += 1
        return pattern_map


Solution().minWindow("ADOBECODEBANC", "ABC")
