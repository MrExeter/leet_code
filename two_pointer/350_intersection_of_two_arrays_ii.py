from typing import List

class Solution:
    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     # First Solution
    #     freq1, freq2 = dict(), dict()
    #     for num in nums1:
    #         freq1[num] = freq1.get(num, 0) + 1
    #     for num in nums2:
    #         freq2[num] = freq2.get(num, 0) + 1
    #
    #     common = []
    #
    #     for key, freq in freq1.items():
    #         tmp = []
    #         if key in freq2:
    #             min_count = min(freq1[key], freq2[key])
    #             tmp = [key] * min_count
    #
    #         if len(tmp) > 0:
    #             common = common + [item for item in tmp]
    #
    #     return common


    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     # Better, faster solution, bad on memory
    #     freq1, freq2 = dict(), dict()
    #
    #     # Count the frequency of elements in nums1
    #     for num in nums1:
    #         freq1[num] = freq1.get(num, 0) + 1
    #
    #     # Count the frequency of elements in nums2
    #     for num in nums2:
    #         freq2[num] = freq2.get(num, 0) + 1
    #
    #     common = []
    #
    #     # Find the common elements and add them to the result
    #     for key in freq1:
    #         if key in freq2:
    #             min_count = min(freq1[key], freq2[key])
    #             common.extend([key] * min_count)
    #
    #     return common

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Two pointer method, better on memory, slightly slower performance
        nums1.sort()
        nums2.sort()

        i, j = 0, 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return result


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    sol = Solution()
    ans = sol.intersect(nums1, nums2)
    print(ans)