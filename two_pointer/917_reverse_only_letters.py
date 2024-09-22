class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        if len(s) < 2:
            return s

        let_arr = [c for c in s]

        left, right = 0, len(let_arr) - 1
        while left <= right:
            if let_arr[left].isalpha() and let_arr[right].isalpha():
                let_arr[left], let_arr[right] = let_arr[right], let_arr[left]
                left += 1
                right -= 1
            elif not let_arr[left].isalpha():
                left += 1
            elif not let_arr[right].isalpha():
                right -= 1

        return ''.join(let_arr)



if __name__ == '__main__':
    # s = "ab-cd"
    # s = "a-bC-dEf-ghIj"
    s = "a"

    sol = Solution()
    ans = sol.reverseOnlyLetters(s)
    print(ans)
