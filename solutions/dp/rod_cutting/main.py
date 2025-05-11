class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()

        memo = {}

        def solve(cuts_start, cuts_end, left, right):
            if cuts_start > cuts_end:
                return 0

            min_cost = None
            for i in range(cuts_start, cuts_end+1):
                c = cuts[i]
                if c > left and c < right:
                    if (left, c) in memo:
                        left_cost = memo[(left, c)]
                    else:
                        left_cost = solve(cuts_start, i, left, c)
                        memo[(left, c)] = left_cost

                    if (c, right) in memo:
                        right_cost = memo[(c, right)]
                    else:
                        right_cost = solve(i, cuts_end, c, right)
                        memo[(c, right)] = right_cost

                    cost = left_cost + right_cost
                    min_cost = min(min_cost, cost) if min_cost is not None else cost
            if min_cost is None:
                return 0
            return min_cost + (right - left)

        return solve(0, len(cuts)-1, 0, n)
