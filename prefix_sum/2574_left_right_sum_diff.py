from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum = [0] + [sum(nums[:i]) for i in range(1, len(nums))]
        rightsum = [sum(nums[i:]) for i in range(1, len(nums))] + [0]
        out = [abs(leftsum[i] - rightsum[i]) for i in range(0, len(nums))]
        return out

    # def leftRightDifference(self, nums: List[int]) -> List[int]:
        # prefix = [0]
        # for x in nums:
        #     prefix.append(prefix[-1] + x)
        #
        # after = [0]
        # for x in nums[::-1]:
        #     after.append(after[-1] + x)
        # after.reverse()
        #
        # answer = [0] * len(nums)
        # for i in range(len(nums)):
        #     answer[i] = abs(prefix[i] - after[i + 1])
        #
        # return answer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sol = Solution()
    arr = [10, 4, 8, 3]

    ans = sol.leftRightDifference(arr)
    print(ans)


