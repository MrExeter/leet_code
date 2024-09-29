"""
You are given an array of characters letters that is sorted in non-decreasing order, and a character target.
There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target.
If such a character does not exist, return the first character in letters.

Constraints:

    2 <= letters.length <= 104
    letters[i] is a lowercase English letter.
    letters is sorted in non-decreasing order.
    letters contains at least two different characters.
    target is a lowercase English letter.

"""
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        left, right = 0, len(letters) - 1

        while left <= right:
            mid = (left + right) // 2

            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return letters[left % len(letters)]


if __name__ == '__main__':
    # letters = ["c", "f", "j"]
    # target = "a"

    letters = ["c", "f", "j"]
    target = "c"

    # letters = ["x", "x", "y", "y"]
    # target = "z"

    sol = Solution()
    ans = sol.nextGreatestLetter(letters, target)
    print(ans)
