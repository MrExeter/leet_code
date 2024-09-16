"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

    "a->b" if a != b
    "a" if a == b


Constraints:

    0 <= nums.length <= 20
    -2^31 <= nums[i] <= 2^31 - 1
    All the values of nums are unique.
    nums is sorted in ascending order.

"""

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        out = []
        start = 0

        if not nums:
            return out

        for i in range(1, len(nums) + 1):
            debug = 99
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                if start == i - 1:
                    out.append(str(nums[start]))
                else:
                    out.append(f'{nums[start]}->{nums[i - 1]}')

                start = i

        return out



if __name__ == "__main__":
    nums = [0, 1, 2, 4, 5, 7]

    sol = Solution()
    ans = sol.summaryRanges(nums)
    print(ans)
