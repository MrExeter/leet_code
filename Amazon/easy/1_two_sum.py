from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # First solution
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # Second solution -- SMART SOLUTION
        my_dict = dict()
        for i in range(len(nums)):
            my_dict[nums[i]] = i

        for i, num in enumerate(nums):
            if target - num in my_dict:
                if i != my_dict[target - num]:
                    return [i, my_dict.get(target - num)]


if __name__ == '__main__':
    # arr = [2, 7, 11, 15]
    # tar = 9

    arr = [3, 2, 4]
    tar = 6



    sol = Solution()
    ans = sol.twoSum(arr, tar)
    print(ans)
