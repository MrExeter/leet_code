class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        pivot = -1
        if word.count(ch) != 0:
            pivot = word.index(ch)

        left, right = 0, pivot
        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1

        return ''.join(word)


if __name__ == '__main__':
    sol = Solution()
    wrd = "abcdefd"
    cr = "d"

    ans = sol.reversePrefix(wrd, cr)
    print(ans)

