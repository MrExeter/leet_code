from collections import defaultdict
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
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # First Solution -- chunky
        freq = dict()
        ptr = head
        while ptr:
            if ptr.val in freq:
                freq[ptr.val] += 1
            else:
                freq[ptr.val] = 1
            ptr = ptr.next

        frequencies = [v for k, v in freq.items()]
        head = ListNode(frequencies[0])
        current = head
        for freq in frequencies[1:]:
            current.next = ListNode(freq)

            current = current.next

        return head

    # def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     # Alternate -- slower
    #     freq = dict()
    #     ptr = head
    #     while ptr:
    #         if ptr.val in freq:
    #             freq[ptr.val] += 1
    #         else:
    #             freq[ptr.val] = 1
    #         ptr = ptr.next
    #
    #     result_head = None
    #     current = None
    #     for count in freq.values():
    #         if result_head is None:
    #             result_head = ListNode(count)  # First node
    #             current = result_head
    #         else:
    #             current.next = ListNode(count)
    #             current = current.next
    #
    #     return result_head







if __name__ == '__main__':

    list = [1,1,2,1,2,3]
    list = list_builder(list)

    sol = Solution()

    ans = sol.frequenciesOfElements(list)
    print(ans)


