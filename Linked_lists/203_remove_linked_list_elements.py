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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Step 1: Remove all head nodes with value `val`
        while head is not None and head.val == val:
            head = head.next

        # Step 2: Traverse the rest of the list
        current = head

        while current is not None and current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return head


if __name__ == '__main__':
    # head = [1, 2, 6, 3, 4, 5, 6]
    # val = 6

    # head = []
    # val = 1

    head = [7, 7, 7, 7]
    val = 7

    # head = [7, 7, 7, 7]
    # val = 5

    # head = [6, 6, 6, 6]
    # val = 6

    head = list_builder(head)

    sol = Solution()
    ans = sol.removeElements(head, val)

    dummy = 99
