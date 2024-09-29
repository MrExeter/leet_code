"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Constraints:

    0 <= x <= 2^31 - 1

"""
from math import floor

class Solution:
    # def mySqrt(self, x: int) -> int:
    #     # Brute Force
    #     root = None
    #     max = x // 2
    #
    #     if x < 1:
    #         return 0
    #
    #     for i in range(1, max + 1):
    #         if i * i <= x:
    #             root = i
    #         else:
    #             break
    #
    #     return int(floor(root))

    def mySqrt(self, x: int) -> int:
        # Binary Search Method
        if x < 2:
            return x
        left, right = 1, x // 2

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        return right


if __name__ == '__main__':
    x = 4
    # x = 8
    # x = 0

    sol = Solution()
    ans = sol.mySqrt(x)
    print(ans)
