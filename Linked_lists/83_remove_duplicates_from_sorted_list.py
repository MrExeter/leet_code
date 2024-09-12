from typing import List, Optional


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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dupe_set = set()
        current = head
        prev = None
        while current:
            value = current.val
            if value not in dupe_set:
                dupe_set.add(value)
                prev = current
                current = current.next

            elif value in dupe_set:
                current = current.next
                prev.next = current

        return head


if __name__ == '__main__':
    # head = [1, 1, 2]

    head = [1, 1, 2, 3, 3]

    # head = [1, 1, 1]

    head = list_builder(head)

    sol = Solution()
    ans = sol.deleteDuplicates(head)

    print(ans)
