"""
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

Constraints:

    1 <= num <= 2^31 - 1

"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        left, right = 1, num

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1
        return False



if __name__ == '__main__':
    # num = 16
    # num = 14
    num = 25

    sol = Solution()
    ans = sol.isPerfectSquare(num)
    print(ans)
