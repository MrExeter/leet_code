class Solution:

    def longestNiceSubstring(self, s: str) -> str:
        # Base case: if the string is too short, it can't be "nice"
        if len(s) < 2:
            return ""

        # Check if the entire string is "nice"
        for i in range(len(s)):
            if (s[i].isupper() and s[i].lower() not in s) or (s[i].islower() and s[i].upper() not in s):
                # If the character doesn't meet the "nice" condition, split the string and check both halves
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])

                # Return the longer of the two "nice" substrings
                return left if len(left) >= len(right) else right

        # If all characters have their counterparts, return the string itself
        return s


if __name__ == '__main__':
    s = "YazaAay"

    sol = Solution()
    ans = sol.longestNiceSubstring(s)

    print(ans)
