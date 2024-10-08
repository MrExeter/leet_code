"""
You have n coins and you want to build a staircase with these coins.
The staircase consists of k rows where the ith row has exactly i coins.
The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Constraints:

    1 <= n <= 2^31 - 1

"""


class Solution:
    def arrangeCoins(self, n: int) -> int:

        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            sum = (mid * (mid + 1)) // 2

            if sum == n:
                return mid
            elif sum < n:
                left = mid + 1
            else:
                right = mid - 1

        return right  # Return 'right' as it will represent the largest complete row

if __name__ == '__main__':
    # n = 3
    # n = 5
    n = 8

    sol = Solution()
    ans = sol.arrangeCoins(n)
    print(ans)