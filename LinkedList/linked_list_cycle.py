"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.


Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Algorithm:
            1. Check if the head is None
            2. Check if the head is in the set
            3. Add the head to the set
            4. Repeat steps 1-3 until the head is None
            5. Return False
        Pattern: Hash Table
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if head is None:
            return False
        seen = set()
        while head is not None:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Algorithm:
            1. Check if the head is None
            2. Set the slow and fast pointers to the head
            3. Repeat steps 4-5 until the fast pointer is None
            4. Set the slow pointer to the next node
            5. Set the fast pointer to the next node twice
            6. Check if the slow and fast pointers are the same
            7. Return the result
        Pattern: Floyd's Tortoise and Hare (Cycle Detection) / Two Pointers
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow is not fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
