from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        avgs = []
        left, right = 0, len(nums) - 1
        while left < right:

            tmp_avg = (nums[left] + nums[right]) / 2

            avgs.append(tmp_avg)
            print(avgs)
            left += 1
            right -= 1

        return min(avgs)


if __name__ == '__main__':
    arr = [1, 9, 8, 3, 10, 5]

    sol = Solution()
    ans = sol.minimumAverage(arr)

    print(ans)
