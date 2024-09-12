from typing import Optional, List


# Definition for singly-linked list.
def find_first_intersection(values1, values2):
    # Find the first common value if it exists
    set_values2 = set(values2)
    for idx1, val in enumerate(values1):
        if val in set_values2:
            idx2 = values2.index(val)
            return idx1, idx2
    return None, None


def build_list(values, intersection_node=None, intersection_index=None):
    # Build the linked list up to the intersection index if provided
    if not values:
        return intersection_node  # If no values, return the shared intersection
    head = ListNode(values[0])
    current = head
    for value in values[1:intersection_index]:
        current.next = ListNode(value)
        current = current.next
    current.next = intersection_node  # Link to the shared node
    return head


def build_shared_part(shared_values):
    # Build the linked list for the shared part (common nodes)
    if not shared_values:
        return None
    head = ListNode(shared_values[0])
    current = head
    for value in shared_values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def build_intersecting_lists(values1, values2):
    idx1, idx2 = find_first_intersection(values1, values2)

    if idx1 is not None:
        # Found an intersection point
        shared_values = values1[idx1:]  # The part that is common in both lists
        shared_node = build_shared_part(shared_values)

        # Build two separate lists leading up to the intersection point
        headA = build_list(values1, shared_node, idx1)
        headB = build_list(values2, shared_node, idx2)
    else:
        # No intersection, build two separate lists
        headA = build_list(values1)
        headB = build_list(values2)

    return headA, headB


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        pA, pB = headA, headB

        while pA != pB:
            # If pA reaches the end of list A, switch to headB, otherwise move forward
            pA = pA.next if pA else headB
            # If pB reaches the end of list B, switch to headA, otherwise move forward
            pB = pB.next if pB else headA


        return pA





if __name__ == '__main__':
    listA = [4, 1, 8, 4, 5]
    listB = [5, 6, 1, 8, 4, 5]

    listA, listB = build_intersecting_lists(listA, listB)

    debug = 99


    # intersectVal = 8
    #
    # skipA = 2
    # skipB = 3
    #
    sol = Solution()
    ans = sol.getIntersectionNode(listA, listB)

    tester = 90


