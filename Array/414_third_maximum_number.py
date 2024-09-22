"""
Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.

Constraints:

    1 <= nums.length <= 10^4
    -2^31 <= nums[i] <= 2^31 - 1


"""


from typing import List


class Solution:

    def thirdMax(self, nums: List[int]) -> int:

        nums = list(set(nums))   # Remove duplicates
        first_max, second_max, third_max = None, None, None

        for num in nums:
            if first_max is None or num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif second_max is None or (num > second_max and num < first_max):
                third_max = second_max
                second_max = num
            elif third_max is None or (num > third_max and num < second_max):
                third_max = num

        if third_max is not None:
            return third_max
        else:
            return first_max


if __name__ == '__main__':
    # nums = [3, 2, 1]

    # nums = [1, 2]

    nums = [2, 2, 3, 1]

    # nums = [1, 2, 2, 5, 3, 5]

    sol = Solution()
    ans = sol.thirdMax(nums)
    print(ans)
