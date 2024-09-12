from typing import List


class Solution:
    # def decrypt(self, code: List[int], k: int) -> List[int]:
    # BRUTE FORCE METHOD
    #     out = []
    #     if k >= 0:
    #         for i in range(len(code)):
    #             tmp = 0
    #             for j in range(i + 1, i + k + 1):
    #                 idx = j % len(code)
    #                 tmp += code[idx]
    #             out.append(tmp)
    #     else:
    #         for i in range(len(code)):
    #             tmp = 0
    #             for j in range(i - 1, i + k - 1, -1):
    #                 idx = j % len(code)
    #                 tmp += code[idx]
    #             out.append(tmp)
    #     return out

    def decrypt(self, code: List[int], k: int) -> List[int]:
        # Elegant Sliding window approach
        n = len(code)

        # If k == 0, all elements are replaced by 0
        if k == 0:
            return [0] * n

        result = [0] * n
        window_sum = 0

        # Determine the range of indices for the sliding window
        start, end = (1, k + 1) if k > 0 else (k, 0)

        # Initialize the window sum for the first element
        for i in range(start, end):
            window_sum += code[i % n]

        # Sliding window
        for i in range(n):
            result[i] = window_sum
            # Slide the window to the next position
            window_sum -= code[(i + start) % n]
            window_sum += code[(i + end) % n]

        return result


if __name__ == '__main__':
    sol = Solution()
    # cde = [5, 7, 1, 4]
    # kay = 3

    # cde = [1, 2, 3, 4]
    # kay = 0

    cde = [2, 4, 9, 3]
    kay = -2

    ans = sol.decrypt(cde, kay)

    print(ans)
