"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Constraints:

1 <= k <= points.length <= 104
-104 < xi, yi < 104
"""

from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Algorithm:
            1. sort the points based on the distance from the origin
            2. return the first k points
        Pattern: Sorting
        Time Complexity: O(nlogn)
        Space Complexity: O(n)
        """
        return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:k]


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Algorithm:
            1. Create a max heap of size k
            2. Iterate over the points
            3. If the heap is not full, add the point to the heap
            4. If the heap is full, compare the distance of the point with the distance of the top of the heap
            5. If the distance of the point is less than the distance of the top of the heap, pop the top of the heap and add the point to the heap
            6. Return the heap
        Pattern: Heap
        Time Complexity: O(nlogk)
        Space Complexity: O(k)
        """
        import heapq

        heap = []
        for point in points:
            heapq.heappush(heap, (point[0] ** 2 + point[1] ** 2, point))
        return [heapq.heappop(heap)[1] for _ in range(k)]
