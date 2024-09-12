# Definition for singly-linked list.
from typing import Optional, List


def list_builder(values: List[int]):
    # Helper function to construct a linked list, so i can mimic the LeetCode tests
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)

        current = current.next

    return head


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node
        dummy_node = ListNode()
        tail = dummy_node

        # Traverse both lists
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1  # Attach list1 node to the result
                list1 = list1.next  # Move list1 to its next node
            else:
                tail.next = list2  # Attach list2 node to the result
                list2 = list2.next  # Move list2 to its next node

            tail = tail.next  # Move the tail to the newly added node

        # Attach the remaining nodes from either list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # Return the merged list, skipping the dummy node
        return dummy_node.next


if __name__ == '__main__':


    list1 = [1, 2, 4]
    list2 = [1, 3, 4]

    list1 = list_builder(list1)
    list2 = list_builder(list2)

    sol = Solution()
    ans = sol.mergeTwoLists(list1, list2)

    print(ans)


