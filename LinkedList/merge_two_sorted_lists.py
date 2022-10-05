"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

Answer: Use two pointers to traverse the two lists. Compare the values of the nodes pointed by the two pointers. Add the node with the smaller value to the merged list. Move the pointer of the list with the smaller value to the next node. Repeat until one of the two lists is empty. Then, add the remaining nodes of the other list to the merged list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{self.val} -> {self.next}"

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a new list
        new_list = ListNode()

        # Create a pointer to the new list
        new_list_pointer = new_list

        # While both lists are not empty
        while l1 is not None and l2 is not None:
            # If the value of the first list is less than or equal to the value of the second list
            if l1.val <= l2.val:
                # Append the value of the first list to the new list
                new_list_pointer.next = ListNode(l1.val)
                # Move the pointer of the first list to the next node
                l1 = l1.next

            # If the value of the second list is less than the value of the first list
            else:
                # Append the value of the second list to the new list
                new_list_pointer.next = ListNode(l2.val)
                # Move the pointer of the second list to the next node
                l2 = l2.next
            # Move the pointer of the new list to the next node
            new_list_pointer = new_list_pointer.next

        # If the first list is empty
        if l1 is None:
            # Append the second list to the new list
            new_list_pointer.next = l2

        # If the second list is empty
        if l2 is None:
            # Append the first list to the new list
            new_list_pointer.next = l1

        # Return the new list
        return new_list.next
