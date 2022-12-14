"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.


Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105

Answer: Use a while loop to find the start index of the new interval. Use a while loop to find the end index of the new interval. Insert the new interval into the intervals array. Merge the intervals array.
"""

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
        Algorithm:
            1. Use a while loop to find the start index of the new interval.
            2. Use a while loop to find the end index of the new interval.
            3. Insert the new interval into the intervals array.
            4. Merge the intervals array.
        Pattern: Two Pointers
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        result = []
        i = 0
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            result += (intervals[i],)
            i += 1
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1]),
            ]
            i += 1
        result.append(newInterval)
        result.extend(intervals[i:])
        return result
