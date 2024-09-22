"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Constraints:

    n == nums.length
    1 <= n <= 10^4
    0 <= nums[i] <= n
    All the numbers of nums are unique.

"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum numbers between 1 to n, then subtract the actual sum of nums
        actual_sum = sum(nums)
        n = len(nums)
        expected_sum = n * (n + 1) // 2

        return expected_sum - actual_sum


if __name__ == '__main__':
    # nums = [3, 0, 1]

    # nums = [0, 1]
    nums = [1, 2]

    # nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

    sol = Solution()
    ans = sol.missingNumber(nums)
    print(ans)
