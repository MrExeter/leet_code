"""
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed,
and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name,
with some characters (possibly none) being long pressed.

Constraints:

    1 <= name.length, typed.length <= 1000
    name and typed consist of only lowercase English letters.

"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0

        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False

            j += 1

        return i == len(name)



if __name__ == '__main__':

    # name = "alex"
    # typed = "aaleex"

    # name = "saeed"
    # typed = "ssaaedd"

    # name = "alex"
    # typed = "aaleexa"

    name = "abcd"
    typed = "aaabbbcccddd"

    sol = Solution()
    ans = sol.isLongPressedName(name, typed)
    print(ans)


