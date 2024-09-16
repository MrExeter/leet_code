"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Constraints:

    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9

"""


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)

        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]

    sol = Solution()
    ans = sol.containsDuplicate(nums)

    print(ans)
