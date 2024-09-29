"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
your product fails the quality check. Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the
first bad version. You should minimize the number of calls to the API.

Constraints:

    1 <= bad <= n <= 2^31 - 1

"""


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2
            api_call = isBadVersion(mid)

            if api_call:
                right = mid  # Narrow down to the first bad version
            else:
                left = mid + 1  # Continue searching in the right half

        return left  # left will be at the first bad version


if __name__ == '__main__':
    n = 5

    sol = Solution()
    ans = sol.firstBadVersion(n)
    print(ans)


