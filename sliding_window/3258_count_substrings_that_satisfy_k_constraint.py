class Solution:
    # def countKConstraintSubstrings(self, s: str, k: int) -> int:
        # Brute Force, works but is inefficient
        # count = 0
        # for left in range(len(s)):
        #     for right in range(left, len(s)):
        #         if s[left:right+1].count('0') <= k or s[left:right+1].count('1') <= k:
        #             count += 1
        # return count

    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        # Smarter sliding window
        left = 0
        count_0 = 0
        count_1 = 0
        total_subs = 0

        # Outer loop to move the `right` pointer
        for right in range(len(s)):
            # Update the counts based on the character at `s[right]`
            if s[right] == '0':
                count_0 += 1
            else:
                count_1 += 1

            # While the window violates the k constraint, move the `left` pointer to shrink the window
            while count_0 > k and count_1 > k:
                if s[left] == '0':
                    count_0 -= 1
                else:
                    count_1 -= 1
                left += 1

            # Count all valid substrings ending at `right`
            total_subs += right - left + 1

        return total_subs


def countKConstraintSubstrings(self, s: str, k: int) -> int:
    sol = Solution()
    ans = sol.countKConstraintSubstrings(stt, kay)
    print(ans)
