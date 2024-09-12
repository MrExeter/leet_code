from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # # First Solution
        # a, b = len(nums1), len(nums2)
        # out = []
        # if a <= b:
        #     out = [nums1[n] for n in range(a) if nums1[n] in nums2]
        # else:
        #     out = [nums2[n] for n in range(b) if nums2[n] in nums1]
        #
        # return list(set(out))

        # Snarter solution
        nums1_set = set(nums1)
        out = []
        for n in nums1_set:
            if n in nums2:
                out.append(n)

        return out



if __name__ == '__main__':
    nums_1 = [1, 2, 2, 1]
    nums_2 = [2, 2]

    sol = Solution()
    ans = sol.intersection(nums_1, nums_2)
    print(ans)

