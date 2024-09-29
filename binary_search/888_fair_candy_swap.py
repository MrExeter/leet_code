"""
Alice and Bob have a different total number of candies. You are given two integer arrays aliceSizes and bobSizes
where aliceSizes[i] is the number of candies of the ith box of candy that Alice has and bobSizes[j] is the number
of candies of the jth box of candy that Bob has.

Since they are friends, they would like to exchange one candy box each so that after the exchange, they both have the
same total amount of candy. The total amount of candy a person has is the sum of the number of candies in each box they have.

Return an integer array answer where answer[0] is the number of candies in the box that Alice must exchange,
and answer[1] is the number of candies in the box that Bob must exchange. If there are multiple answers,
you may return any one of them. It is guaranteed that at least one answer exists.


Constraints:

    1 <= aliceSizes.length, bobSizes.length <= 10^4
    1 <= aliceSizes[i], bobSizes[j] <= 10^5
    Alice and Bob have a different total number of candies.
    There will be at least one valid answer for the given input.

"""

from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA, sumB = sum(aliceSizes), sum(bobSizes)
        setB = set(bobSizes)

        delta = (sumB - sumA) // 2

        for candy in aliceSizes:
            y = candy + delta
            if y in setB:
                return [candy, y]

        debug = 99


if __name__ == "__main__":
    # aliceSizes = [1, 1]
    # bobSizes = [2, 2]

    aliceSizes = [1, 2]
    bobSizes = [2, 3]

    # aliceSizes = [2]
    # bobSizes = [1, 3]

    sol = Solution()
    ans = sol.fairCandySwap(aliceSizes, bobSizes)
    print(ans)
