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
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     # First Solution
    #     vals = []
    #     pA = head
    #     while pA.next:
    #         vals.append(pA.val)
    #         pA = pA.next
    #     vals.append(pA.val)
    #     return vals == vals[::-1]
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # This method uses fast and slow pointers,
        # This finds the midpoint of the list, reverse the midpoint to the end
        # and compare the elements from the first half to the reversed second half node by node
        p_slow, p_fast = head, head

        while p_fast and p_fast.next:
            p_slow = p_slow.next
            p_fast = p_fast.next.next

        # p_slow: Found the midpoint, reverse the list from the midpoint til then end and compare to values
        prev = None
        current = p_slow
        while current:
            next = current.next
            current.next = prev
            prev, current = current, next

        first_half = head
        second_half = prev

        # Compare front half to reversed second half
        while second_half:
            if first_half.val != second_half.val:
                return False

            first_half = first_half.next
            second_half = second_half.next

        return True






if __name__ == '__main__':
    list = [1, 2, 2, 1]
    # list = [1, 2, 1]

    # list = [1, 2, 3, 4, 5]
    list = list_builder(list)

    sol = Solution()
    ans = sol.isPalindrome(list)
    print(ans)
