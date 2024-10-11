"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element
of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.


Constraints:

    1 <= nums1.length <= nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 10^4
    All integers in nums1 and nums2 are unique.
    All the integers of nums1 also appear in nums2.

"""
from typing import List


class Solution:
    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     # Slow Brute force method
    #     out = []
    #     for i in range(len(nums1)):
    #         tmp2 = nums1[i]
    #         found = False  # Track if we've found the next greater element
    #         if tmp2 in nums2:
    #             for j in range(nums2.index(tmp2) + 1, len(nums2)):
    #                 if nums2[j] > tmp2:
    #                     out.append(nums2[j])
    #                     found = True  # Mark that we found a greater element
    #                     break
    #         if not found:
    #             out.append(-1)  # If no greater element is found, append -1
    #     return out

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # More efficient method using a hash table
        next_greater_stack = []
        next_greater_map = {}

        for num in nums2:
            while len(next_greater_stack) > 0 and num > next_greater_stack[-1]:
                elem = next_greater_stack.pop()
                next_greater_map[elem] = num
            next_greater_stack.append(num)

        for elem in next_greater_stack:
            next_greater_map[elem] = -1

        result = []
        for num in nums1:
            result.append(next_greater_map[num])

        return result



if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]

    # nums1 = [2, 4]
    # nums2 = [1, 2, 3, 4]

    # nums1 = [3, 1, 5, 7, 9, 2, 6]
    # nums2 = [1, 2, 3, 5, 6, 7, 9, 11]

    sol = Solution()
    ans = sol.nextGreaterElement(nums1, nums2)
    print(ans)
