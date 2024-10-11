"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of
all the integers in the range [1, n] that do not appear in nums.

Constraints:

    n == nums.length
    1 <= n <= 105
    1 <= nums[i] <= n

"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numz_set = set(nums)  # Keep nums as a set for O(1) lookup
        result = [i for i in range(1, len(nums) + 1) if i not in numz_set]
        return result


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]

    # nums = [1, 1]

    # nums = [2, 2]

    sol = Solution()
    ans = sol.findDisappearedNumbers(nums)
    print(ans)
