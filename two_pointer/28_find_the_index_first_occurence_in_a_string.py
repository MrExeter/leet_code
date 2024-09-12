
class Solution:
    # def strStr(self, haystack: str, needle: str) -> int:
    #     # First Method
    #     return haystack.find(needle)

    def strStr(self, haystack: str, needle: str) -> int:
        # First approach
        # if len(needle) > len(haystack):
        #     return -1
        #
        # if len(haystack) == 1 and len(needle) == 1:
        #     if haystack == needle:
        #         return 0
        #     else:
        #         return -1
        #
        # start, end = 0, len(haystack) - len(needle) + 1
        #
        # for i in range(start, end):
        #     tmp = haystack[i: i + len(needle)]
        #     if haystack[i: i + len(needle)] == needle:
        #         return i
        # return -1

        if len(needle) > len(haystack):
            return -1

        if len(haystack) == 1 and len(needle) == 1:
            return 0 if haystack == needle else -1

        for i in range(len(haystack) - len(needle) + 1):
            match = True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i
        return -1


if __name__ == '__main__':
    # haystack = "sadbutsad"
    # needle = "sad"

    # haystack = "hello"
    # needle = "ll"

    # haystack = "a"
    # needle = "a"

    # haystack = "abc"
    # needle = "c"

    haystack = "leetcode"
    needle = "leeto"

    sol = Solution()
    ans = sol.strStr(haystack, needle)
    print(ans)
