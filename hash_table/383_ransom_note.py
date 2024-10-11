"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters
from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Constraints:

    1 <= ransomNote.length, magazine.length <= 10^5
    ransomNote and magazine consist of lowercase English letters.

"""


class Solution:
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     # First solution
    #     rans = dict()
    #     mags = dict()
    #     result = True
    #
    #     for letter in magazine:
    #         mags[letter] = mags.get(letter, 0) + 1
    #
    #     for letter in ransomNote:
    #         rans[letter] = rans.get(letter, 0) + 1
    #
    #     for k, v in rans.items():
    #         if k not in mags or v > mags[k]:
    #             result = False
    #
    #     return result

    def canConstruct(self, ransomNote, magazine):
        # Single dictionary method
        mags = dict()

        # Count occurrences of each letter in magazine
        for letter in magazine:
            mags[letter] = mags.get(letter, 0) + 1

        # Check if ransomNote can be constructed
        for letter in ransomNote:
            if letter not in mags or mags[letter] == 0:
                return False
            mags[letter] -= 1

        return True


if __name__ == '__main__':
    # ransomNote = "a"
    # magazine = "b"

    # ransomNote = "aa"
    # magazine = "ab"

    ransomNote = "aa"
    magazine = "aab"

    sol = Solution()
    ans = sol.canConstruct(ransomNote, magazine)
    print(ans)



