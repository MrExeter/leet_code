from typing import List

"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Constraints:

1 <= nums.length <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4
Each element in the array appears twice except for one element which appears only once.

"""

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         # This works, but doesn't use constant space
#         freq_dict = dict()
#         for num in nums:
#             freq_dict[num] = freq_dict.get(num, 0) + 1
#
#         return min(freq_dict, key=freq_dict.get)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Better solution
        result = 0
        for num in nums:
            result ^= num
        return result



if __name__ == '__main__':
    nums = [2, 2, 1]

    sol = Solution()
    ans = sol.singleNumber(nums)

    print(ans)
