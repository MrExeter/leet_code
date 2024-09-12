class Solution:
    # def pivotInteger(self, n: int) -> int:
    #     arr = [i for i in range(1, n + 1)]
    #     arr.reverse()
    #     idx = -1
    #     while idx < len(arr):
    #         idx += 1
    #         if sum(arr[0: idx + 1]) == sum(arr[idx:]):
    #             return arr[idx]
    #     return -1

    def pivotInteger(self, n: int) -> int:
        sum1 = 0
        tot_sum = sum(range(1, n+1))
        for x in range(1, n + 1):
            sum1 += x
            if 2 * sum1 == tot_sum + x:
                return x
        return -1




if __name__ == '__main__':
    sol = Solution()
    n = 8
    ans = sol.pivotInteger(n)
    print(ans)