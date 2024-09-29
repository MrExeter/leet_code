"""
Given an integer array nums sorted in non-decreasing order and an integer target, return true if target is a majority
element, or false otherwise.

A majority element in an array nums is an element that appears more than nums.length / 2 times in the array.

Constraints:

    1 <= nums.length <= 1000
    1 <= nums[i], target <= 109
    nums is sorted in non-decreasing order.

"""
from bisect import bisect_right, bisect_left
from typing import List


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        start = bisect_left(nums, target)
        end = bisect_right(nums, target)

        # Calculate the count of 'target'
        count = end - start

        # Check if it appears more than half the length of the array
        return count > len(nums) // 2


if __name__ == '__main__':
    nums = [2, 4, 5, 5, 5, 5, 5, 6, 6]
    target = 5

    sol = Solution()
    ans = sol.isMajorityElement(nums, target)
    print(ans)
