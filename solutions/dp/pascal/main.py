from typing import List


class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        for row in range(1, numRows):
            prev_row = triangle[-1]
            new_row = [1]
            for col in range(1, row):
                new_row.append(prev_row[col] + prev_row[col - 1])
            new_row.append(1)
            triangle.append(new_row)

        return triangle

    def generate_cleaner(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        prev_row = triangle[0]

        for row in range(1, numRows):
            new_row = [1]
            for col in range(1, row):
                new_row.append(prev_row[col] + prev_row[col - 1])
            new_row.append(1)
            triangle.append(new_row)
            prev_row = new_row

        return triangle

    def generate_iter(self, numRows: int) -> List[List[int]]:
        dp = [[0] * (i + 1) for i in range(numRows + 1)]

        results = []
        for row in range(1, numRows + 1):
            rowResult = []
            for col in range(1, row + 1):
                if row == 1:
                    dp[row][col] = 1
                elif col == 1 or col == row:
                    dp[row][col] = 1
                else:
                    dp[row][col] = dp[row - 1][col] + dp[row - 1][col - 1]
                rowResult.append(dp[row][col])
            results.append(rowResult)
        return results

    def generate_recur(self, numRows: int) -> List[List[int]]:
        def solve(row, col):
            if col == 1 or col == row:
                return 1
            return solve(row - 1, col - 1) + solve(row - 1, col)

        allResults = []
        for r in range(1, numRows + 1):
            results = []
            for c in range(1, r + 1):
                results.append(solve(r, c))
            allResults.append(results)

        return allResults


print(Solution().generate(5))
