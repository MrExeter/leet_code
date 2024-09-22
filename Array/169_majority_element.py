"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Constraints:

    n == nums.length
    1 <= n <= 5 * 10^4
    -10^9 <= nums[i] <= 10^9

"""


from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_dict = dict()
        for i in range(len(nums)):
            if nums[i] in majority_dict:
                majority_dict[nums[i]] += 1
            else:
                majority_dict[nums[i]] = 1

        return max(majority_dict, key=majority_dict.get)


if __name__ == '__main__':
    # nums = [3, 2, 3]
    nums = [6, 5, 5]

    sol = Solution()
    ans = sol.majorityElement(nums)
    print(ans)
