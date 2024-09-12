class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        dict_st, dict_ts = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if ((c1 in dict_st) and dict_st[c1] != c2) or ((c2 in dict_ts) and dict_ts[c2] != c1):
                return False
            dict_st[c1] = c2
            dict_ts[c2] = c1

        return True


if __name__ == '__main__':
    # s1 = "egg"
    # s2 = "add"

    # s1 = "foo"
    # s2 = "bar"

    # s1 = "paper"
    # s2 = "title"

    s1 = "bbbaaaba"
    s2 = "aaabbbba"



    sol = Solution()
    ans = sol.isIsomorphic(s1, s2)

    print(ans)