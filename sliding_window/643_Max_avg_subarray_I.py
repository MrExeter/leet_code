from typing import List


class Solution:
    # def findMaxAverage(self, nums: List[int], k: int) -> float:
    #     max_avg = float("-inf")
    #
    #     tmp_sum = 0
    #     for i in range(len(nums)):
    #
    #         tmp_sum += nums[i]
    #         print(i, tmp_sum, max_avg)
    #         if i >= k - 1:
    #             max_avg = max(max_avg, tmp_sum / k)
    #             tmp_sum -= nums[i - k + 1]
    #
    #     return max_avg

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < 2:
            return nums[0]

        max_avg = float("-inf")
        idx = 0
        tmp_sum = 0
        while idx < len(nums) - k + 1:
            print(idx)
            if idx == 0:
                tmp_sum = sum(nums[idx: k])
                max_avg = tmp_sum / k

            else:
                tmp_sum = tmp_sum + nums[idx + k - 1] - nums[idx - 1]
                max_avg = max(max_avg, tmp_sum / k)

            idx += 1

        return max_avg

if __name__ == '__main__':
    sol = Solution()
    # arr = [1, 12, -5, -6, 50, 3]
    # k = 4

    arr = [5]
    k = 1

    # arr = [0, 1, 1, 3, 3]
    # k = 4

    # arr = [8860, -853, 6534, 4477, -4589, 8646, -6155, -5577, -1656, -5779, -2619, -8604, -1358, -8009, 4983, 7063,
    #        3104, -1560, 4080, 2763, 5616, -2375, 2848, 1394, -7173, -5225, -8244, -809, 8025, -4072, -4391, -9579, 1407,
    #        6700, 2421, -6685, 5481, -1732, -8892, -6645, 3077, 3287, -4149, 8701, -4393, -9070, -1777, 2237, -3253,
    #        -506, -4931, -7366, -8132, 5406, -6300, -275, -1908, 67, 3569, 1433, -7262, -437, 8303, 4498, -379, 3054,
    #        -6285, 4203, 6908, 4433, 3077, 2288, 9733, -8067, 3007, 9725, 9669, 1362, -2561, -4225, 5442, -9006, -429,
    #        160, -9234, -4444, 3586, -5711, -9506, -79, -4418, -4348, -5891]
    # k = 93
    ans = sol.findMaxAverage(arr, k)
    print(ans)
