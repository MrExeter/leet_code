class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        count = 1

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)

        result = 0
        for i in range(1, len(groups)):
            result += min(groups[i], groups[i - 1])

        return result




if __name__ == '__main__':
    s = "00110011"

    sol = Solution()
    ans = sol.countBinarySubstrings(s)
    print(ans)