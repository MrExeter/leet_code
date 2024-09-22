from math import inf
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        out = []
        last_seen_c = -inf

        for i in range(len(s)):
            if s[i] == c:
                last_seen_c = i
            out.append(abs(last_seen_c - i))

        last_seen_c = -inf
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                last_seen_c = i
            out[i] = min(out[i], abs(last_seen_c - i))

        return out

if __name__ == '__main__':
    s = "loveleetcode"
    c = "e"

    sol = Solution()
    ans = sol.shortestToChar(s, c)

    print(ans)

