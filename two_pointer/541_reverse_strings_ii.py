class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # s_arr = list(s)
        #
        # left = 0
        # right = left + k - 1
        # if 1 < k < len(s_arr):
        #     while right < len(s_arr):
        #         if left < right:
        #             s_arr[left], s_arr[right] = s_arr[right], s_arr[left]
        #             left += 1
        #             right -= 1
        #         else:
        #             left += 2 * k - 1
        #             right += left + k - 1
        #
        # elif k >= len(s_arr):
        #     s_arr = s_arr[::-1]
        #
        # return ''.join(s_arr)
        s_arr = list(s)

        left = 0
        while left < len(s_arr):
            # Right pointer should reverse only the first k characters, so ensure it stays within bounds
            right = min(left + k - 1, len(s_arr) - 1)

            # Reverse the first k characters using two pointers
            l, r = left, right
            while l < r:
                s_arr[l], s_arr[r] = s_arr[r], s_arr[l]
                l += 1
                r -= 1

            # Move left pointer forward by 2k to process the next chunk
            left += 2 * k

        return ''.join(s_arr)


if __name__ == '__main__':

    # s = "abcdefg"
    # k = 2

    # s = "abcd"
    # k = 2

    # s = "abcdefg"
    # k = 1

    # s = "abcdefg"
    # k = 8

    s = "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"

    k = 39

    sol = Solution()
    ans = sol.reverseStr(s, k)
    print(ans)
