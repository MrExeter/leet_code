from typing import List


class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:

        score = 0
        total = sum(calories[:k])  # Calculate the sum of the first 'k' days

        for start in range(len(calories) - k + 1):
            # Check the total for the current window
            if total < lower:
                score -= 1
            elif total > upper:
                score += 1

            # Slide the window: adjust total sum for next window
            if start + k < len(calories):
                total = total - calories[start] + calories[start + k]

        return score


if __name__ == '__main__':

    # calories = [1, 2, 3, 4, 5]
    # k = 1
    # lower = 3
    # upper = 3
    # Output: 0

    # calories = [3, 2]
    # k = 2
    # lower = 0
    # upper = 1
    # Output: 0

    calories = [6, 5, 0, 0]
    k = 2
    lower = 1
    upper = 5
    Output: 0

    sol = Solution()
    ans = sol.dietPlanPerformance(calories, k, lower, upper)
    print(ans)

