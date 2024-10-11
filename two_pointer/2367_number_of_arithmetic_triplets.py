"""
You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

    i < j < k,
    nums[j] - nums[i] == diff, and
    nums[k] - nums[j] == diff.

Return the number of unique arithmetic triplets.

Constraints:

    3 <= nums.length <= 200
    0 <= nums[i] <= 200
    1 <= diff <= 50
    nums is strictly increasing.

"""


from typing import List


class Solution:
    # def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
    #     # Brute Force method
    #     count = 0
    #     for i in range(len(nums) - 2):
    #         for j in range(i + 1, len(nums) - 1):
    #             for k in range(j + 1, len(nums)):
    #                 if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
    #                     count += 1
    #     return count

    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # Much faster and efficient solution
        num_set = set(nums)
        count = 0
        for num in nums:
            if num + diff in num_set and num + 2 * diff in num_set:
                count += 1

        return count


if __name__ == '__main__':
    sol = Solution()
    nums = [0, 1, 4, 6, 7, 10]
    diff = 3

    ans = sol.arithmeticTriplets(nums, diff)
    print(ans)
