"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

    Each letter in pattern maps to exactly one unique word in s.
    Each unique word in s maps to exactly one letter in pattern.
    No two letters map to the same word, and no two words map to the same letter.


Constraints:

    1 <= pattern.length <= 300
    pattern contains only lower-case English letters.
    1 <= s.length <= 3000
    s contains only lowercase English letters and spaces ' '.
    s does not contain any leading or trailing spaces.
    All the words in s are separated by a single space.

"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        dict_st, dict_ts = {}, {}

        if len(pattern) != len(s):
            return False

        for i in range(len(s)):
            c1, c2 = pattern[i], s[i]
            if ((c1 in dict_st) and dict_st[c1] != c2) or ((c2 in dict_ts) and dict_ts[c2] != c1):
                return False
            dict_st[c1] = c2
            dict_ts[c2] = c1

        return True


if __name__ == '__main__':
    # pattern = "abba"
    # s = "dog cat cat dog"

    # pattern = "abba"
    # s = "dog cat cat fish"

    # pattern = "aaaa"
    # s = "dog cat cat dog"

    # pattern = 'abba'
    # s = "dog dog dog dog"

    pattern = "aaa"
    s = "aa aa aa aa"

    sol = Solution()
    ans = sol.wordPattern(pattern, s)
    print(ans)
