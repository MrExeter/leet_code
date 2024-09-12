from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_tot = 0
        for k, v in counts.items():
            if (k + 1) in counts:
                tot = counts[k] + counts[k + 1]
                if tot > max_tot:
                    max_tot = tot

        return max_tot


if __name__ == '__main__':
    # nums = [1, 3, 2, 2, 5, 2, 3, 7]
    # Output: 5

    # nums = [1, 2, 3, 4]
    # Output: 2

    nums = [1, 1, 1, 1]
    Output: 0
    # nums = [1, 2, 2, 3, 4, 5, 1, 1, 1, 1]
    # output = 7

    sol = Solution()
    ans = sol.findLHS(nums)

    print(ans)
