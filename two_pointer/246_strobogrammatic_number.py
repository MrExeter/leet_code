class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        map_dict = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        for c in '23457':
            if c in num:
                return False

        left, right = 0, len(num) - 1
        while left <= right:
            if num[left] != map_dict.get(num[right]):
                return False
            left += 1
            right -= 1

        return True



if __name__ == '__main__':

    num = '69'
    # num = "88"
    # num = '962'
    sol = Solution()
    ans = sol.isStrobogrammatic(num)

    print(ans)
