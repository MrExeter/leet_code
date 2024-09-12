from typing import List, Optional


# Definition for singly-linked list.


def list_builder(values: List[int], pos: int):
    # Helper function to construct a linked list with a cycle at 'pos'
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    target = None  # This will store the node to which we need to link to create the cycle

    # If pos is 0, the cycle should point to the head
    if pos == 0:
        target = head

    # Build the linked list
    for i, value in enumerate(values[1:], 1):
        current.next = ListNode(value)
        current = current.next
        # Save the target node for the cycle
        if i == pos:
            target = current
    # If pos != -1, link the last node's next to the target to form a cycle
    if pos != -1:
        current.next = target

    return head


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = fast = head
        while fast and fast.next:
            slow = slow.next  # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps

            if slow == fast:  # If they meet, there's a cycle
                return True

        return False  # No cycle if fast reaches the end


if __name__ == '__main__':
    head = [3, 2, 0, -4]
    pos = 1
    #
    # head = [1]
    # pos = -1

    head = list_builder(head, pos)
    sol = Solution()
    ans = sol.hasCycle(head)

    print(ans)
