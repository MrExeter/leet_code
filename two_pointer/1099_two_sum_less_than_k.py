from typing import List


class Solution:
    # def twoSumLessThanK(self, nums: List[int], k: int) -> int:
    #     # Brute Force, Turtle solution
    #     nums.sort()
    #     tot = -1
    #
    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             tmp = nums[i] + nums[j]
    #             if tmp < k:
    #                 tot = max(tmp, tot)
    #
    #     return tot

    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        tot = -1
        left = 0
        right = len(nums) - 1

        while left < right < len(nums):
            tmp = nums[left] + nums[right]
            if tmp < k:
                left += 1
                tot = max(tot, tmp)
            if tmp >= k:
                right -= 1

        return tot



if __name__ == '__main__':
    nums = [34, 23, 1, 24, 75, 33, 54, 8]
    k = 60

    sol = Solution()
    ans = sol.twoSumLessThanK(nums, k)

    print(ans)
