class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


# 1,2,3 stones = WIN (you can take all)
# 4 stones = LOSE (no matter what you do)
# 5,6,7 stones = WIN (you can force opponent to get 4)
# 8 stones = LOSE (opponent can force you to get 4)
