"""
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements
are within the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of nums
is included in any of the ranges, and each missing number is covered by one of the ranges.

Constraints:

    -10^9 <= lower <= upper <= 10^9
    0 <= nums.length <= 100
    lower <= nums[i] <= upper
    All the values of nums are unique.

"""

from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        out = []

        # Handle case where nums is empty
        if not nums:
            return [[lower, upper]]

        # Check for missing range before the first number
        if nums[0] > lower:
            out.append([lower, nums[0] - 1])

        # Check for missing ranges between consecutive numbers
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                out.append([nums[i - 1] + 1, nums[i] - 1])

        # Check for missing range after the last number
        if upper > nums[-1]:
            out.append([nums[-1] + 1, upper])

        return out


if __name__ == '__main__':
    nums = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99

    # nums = []
    # lower = 0
    # upper = 0

    sol = Solution()
    ans = sol.findMissingRanges(nums, lower, upper)

    print(ans)
