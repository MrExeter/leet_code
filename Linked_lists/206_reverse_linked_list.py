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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        current = head
        while current:

            next = current.next
            current.next = prev

            prev, current = current, next

        return prev


if __name__ == '__main__':
    list = [1, 2, 3, 4, 5]

    list = list_builder(list)

    sol = Solution()
    ans = sol.reverseList(list)

    print(ans)
