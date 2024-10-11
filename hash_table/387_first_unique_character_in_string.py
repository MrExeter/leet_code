"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Constraints:

    1 <= s.length <= 10^5
    s consists of only lowercase English letters.

"""


class Solution:
    # def firstUniqChar(self, s: str) -> int:
    #     # First Solution
    #     let_dict = dict()
    #
    #     for letter in s:
    #         let_dict[letter] = let_dict.get(letter, 0) + 1
    #
    #     lets = [s.index(k) for k, v in let_dict.items() if v == 1]
    #     if len(lets) > 0:
    #         return min(lets)
    #
    #     return -1

    def firstUniqChar(self, s):
        # Better solution, it eliminates the linear search used by index function
        let_dict = {}

        # First pass: Count occurrences of each character
        for letter in s:
            let_dict[letter] = let_dict.get(letter, 0) + 1

        # Second pass: Find the first character with count 1
        for index, letter in enumerate(s):
            if let_dict[letter] == 1:
                return index

        return -1



if __name__ == '__main__':
    # s = "leetcode"

    # s = "loveleetcode"

    s = "aabb"

    sol = Solution()
    ans = sol.firstUniqChar(s)
    print(ans)
