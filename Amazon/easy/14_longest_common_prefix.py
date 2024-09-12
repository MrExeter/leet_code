from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)

        pre = ""

        for i in range(len(strs[0])):
            for word in strs:
                if word[i] != strs[0][i]:
                    return pre
            pre += strs[0][i]

        return pre


if __name__ == '__main__':
    # arr = ["flower", "flow", "flight"]
    arr = ["dog", "racecar", "car"]

    sol = Solution()
    ans = sol.longestCommonPrefix(arr)
    print(ans)
