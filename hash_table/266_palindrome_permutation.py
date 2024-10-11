"""
Given a string s, return true if a permutation of the string could form a
palindrome
and false otherwise.

Constraints:

    1 <= s.length <= 5000
    s consists of only lowercase English letters.

"""


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = {}
        for letter in s:
            freq[letter] = freq.get(letter, 0) + 1

        count = 0
        for v in freq.values():
            if v % 2 != 0:
                count += 1
        return count <= 1


if __name__ == '__main__':
    s = "code"

    # s = "aab"

    sol = Solution()
    ans = sol.canPermutePalindrome(s)
    print(ans)