import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalpha() or c.isalnum()]
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()

    ss = "A man, a plan, a canal: Panama"

    ans = sol.isPalindrome(ss)

    print(ans)
