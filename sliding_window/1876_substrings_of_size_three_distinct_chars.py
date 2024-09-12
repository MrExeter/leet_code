class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0

        count = 0
        idx = 0
        while idx <= len(s) - 3:
            tmp = set()
            tmp.add(ord(s[idx]))
            tmp.add(ord(s[idx + 1]))
            tmp.add(ord(s[idx + 2]))
            if len(tmp) == 3:
                count += 1

            idx += 1
        # for x, y, z in zip(s, s[1:], s[2:]):
        #     if x != y and y != z and x != z:
        #         count += 1
        #
        return count


if __name__ == '__main__':
    sol = Solution()
    s = "xyzzaz"

    ans = sol.countGoodSubstrings(s)

    print(ans)

