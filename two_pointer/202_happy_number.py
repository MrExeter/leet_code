class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            n = self.sum_squares(n)
            if n == 1:
                return True
        return False

    def sum_squares(self, n):
        output = 0
        while n:
            digit = (n % 10)**2
            output += digit
            n = n // 10
        return output


if __name__ == '__main__':
    num = 2
    sol = Solution()
    ans = sol.isHappy(num)
    print(ans)
