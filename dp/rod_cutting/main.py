class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        memo = {}

        def solve(cuts, left, right):
            if len(cuts) == 0:
                return 0

            min_cost = None
            for c in cuts:
                if c > left and c < right:
                    if (left, c) in memo:
                        left_cost = memo[(left, c)]
                    else:
                        left_cost = solve(cuts, left, c)
                        memo[(left, c)] = left_cost

                    if (c, right) in memo:
                        right_cost = memo[(c, right)]
                    else:
                        right_cost = solve(cuts, c, right)
                        memo[(c, right)] = right_cost

                    cost = left_cost + right_cost
                    min_cost = min(min_cost, cost) if min_cost is not None else cost
            if min_cost is None:
                return 0
            return min_cost + (right - left)

        return solve(cuts, 0, n)
