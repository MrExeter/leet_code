"""
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1,1,0] horizontally results in [0,1,1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [0,1,1] results in [1,0,0].

Constraints:

    n == image.length
    n == image[i].length
    1 <= n <= 20
    images[i][j] is either 0 or 1.

"""
from typing import List


class Solution:
    # def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
    #     # First Solution
    #     image = [x[::-1] for x in image]
    #
    #     for row in image:
    #         for i in range(len(row)):
    #             row[i] ^= 1
    #     return image

    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # True Two-Pointer solution
        for row in image:

            left, right = 0, len(image) - 1

            while left <= right:
                # Swap and invert at the same time
                row[left], row[right] = row[right] ^ 1, row[left] ^ 1

                # Move the pointers inward
                left += 1
                right -= 1

        return image


if __name__ == '__main__':
    image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]

    sol = Solution()
    ans = sol.flipAndInvertImage(image)
    print(ans)

