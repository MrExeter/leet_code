"""
Given an array arr of integers, check if there exist two indices i and j such that :

    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

Constraints:

    2 <= arr.length <= 500
    -10^3 <= arr[i] <= 10^3


"""
from typing import List
from bisect import bisect_left

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()

        for i in range(len(arr)):
            chk = 2 * arr[i]

            # Use binary search to find 'chk' in the sorted array
            index = bisect_left(arr, chk)

            # Ensure index is within bounds and isn't the same as `i`
            if index != i and index < len(arr) and arr[index] == chk:
                return True

        return False


if __name__ == '__main__':
    # arr = [10, 2, 5, 3]
    # arr = [3, 1, 7, 11]
    arr = [-2, 0, 10, -19, 4, 6, -8]

    sol = Solution()
    ans = sol.checkIfExist(arr)
    print(ans)
