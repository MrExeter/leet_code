from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # First solution
        # for word in words:
        #     if len(word) == 1:
        #         return word[0]
        #
        #     left, right = 0, len(word) - 1
        #     while left <= right and word[left] == word[right]:
        #         if left + 1 == right:
        #             return word
        #
        #         left += 1
        #         right -= 1
        #         if right == left:
        #             return word
        #
        # return ""

        # Smarter solution
        for word in words:
            tmp = list(word)
            if tmp == tmp[::-1]:
                return word

        return ""



if __name__ == '__main__':
    arr = ["cqllrtyhw", "swwisru", "gpzmbders", "wqibjuqvs", "pp", "usewxryy", "ybqfuh", "hqwwqftgyu", "jggmatpk"]
    # arr = ["x"]
    # arr = ["xyz", "aba"]

    # arr = ["po", "zsz"]

    sol = Solution()
    ans = sol.firstPalindrome(arr)

    print(ans)
