class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


# 1,2,3 stones = WIN (you can take all)
# 4 stones = LOSE (no matter what you do)
# 5,6,7 stones = WIN (you can force opponent to get 4)
# 8 stones = LOSE (opponent can force you to get 4)


# SOME big clues this was solvable through some clever maths...
# The constraint was 1 <= n <= 2^31 - 1. That's a lot of numbers to test!

# The pattern became clear when I just walked through the first 8 numbers.
