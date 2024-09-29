"""
Given an array of distinct integers arr, where arr is sorted in ascending order, return the smallest index i
that satisfies arr[i] == i. If there is no such index, return -1.

Constraints:

    1 <= arr.length < 10^4
    -10^9 <= arr[i] <= 10^9

"""
from typing import List


class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == mid:
                result = mid
                right = mid - 1
            elif arr[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1

        return result


if __name__ == "__main__":
    # arr = [-10, -5, 0, 3, 7]

    # arr = [0, 2, 5, 8, 17]

    # arr = [-10, -5, 3, 4, 7, 9]

    arr = [-10, -5, -2, 0, 4, 5, 6, 7, 8, 9, 10]

    sol = Solution()
    ans = sol.fixedPoint(arr)
    print(ans)
