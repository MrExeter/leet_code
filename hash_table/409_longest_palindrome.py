"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest
palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Constraints:

    1 <= s.length <= 2000
    s consists of lowercase and/or uppercase English letters only.

"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        let_dict = {}
        for letter in s:
            let_dict[letter] = let_dict.get(letter, 0) + 1

        tot = 0
        odd_count = 0
        for count in let_dict.values():
            if count % 2 == 0:
                tot += count  # Add even counts fully
            else:
                tot += count - 1  # Use pairs from odd counts
                odd_count = 1  # Keep track of a single odd letter for the center

        # If there was any odd count, we can add 1 to the total length (for the center)
        return tot + odd_count


if __name__ == '__main__':
    # s = "abccccdd"
    s = "ccc"
    sol = Solution()
    ans = sol.longestPalindrome(s)
    print(ans)



