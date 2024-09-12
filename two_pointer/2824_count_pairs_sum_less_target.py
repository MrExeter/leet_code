from typing import List


class Solution:
    # First Solution
    # def countPairs(self, nums: List[int], target: int) -> int:
    #     count = 0
    #     lnn = len(nums)
    #     for i in range(lnn):
    #         for j in range(i + 1, lnn):
    #             if nums[i] + nums[j] < target:
    #                 count += 1
    #     return count

    def countPairs(self, nums: List[int], target: int) -> int:
        # Smarter Solution
        count = 0
        nums.sort()
        N = len(nums)

        right = N - 1
        for left in range(0, N - 1):
            while right > left and nums[right] + nums[left] >= target:
                right -= 1
            if right <= left:
                break

            count += right - left

        return count



if __name__ == '__main__':
    sol = Solution()
    arr = [-1, 1, 2, 3, 1]

    ans = sol.countPairs(arr, 2)
    print(ans)
