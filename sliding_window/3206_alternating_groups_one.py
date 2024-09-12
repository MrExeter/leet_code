from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count = 0
        if len(colors) < 3:
            return count

        colors = colors + colors[0:2]
        i = 0
        while i < len(colors) - 2:
            if colors[i] != colors[i + 1] and colors[i + 1] != colors[i + 2]:
                count += 1
            i += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    # col = [1, 1, 1]

    col = [0, 1, 0, 0, 1]

    ans = sol.numberOfAlternatingGroups(col)

    print(ans)
