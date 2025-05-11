class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        patterns = 0
        visited = set()

        def move_valid(curr, next):
            nonlocal visited

            if next in visited:
                return False

            if curr == next:
                return False

            curr_row = (curr - 1) // 3
            curr_col = (curr - 1) % 3
            next_row = (next - 1) // 3
            next_col = (next - 1) % 3

            # moving through centre point (diagnonally)
            if abs(curr_col - next_col) == 2 and abs(curr_row - next_row) == 2:
                middle = 5
                return middle in visited

            # moving through centre point (horizontally)
            if curr_row == next_row and abs(curr_col - next_col) == 2:
                middle = (curr + next) // 2
                return middle in visited

            # moving through centre point (vertically)
            if curr_col == next_col and abs(curr_row - next_row) == 2:
                middle = (curr + next) // 2
                return middle in visited

            return True

        def backtrack(digit, count):
            nonlocal patterns

            if count > n:  # exceeded max length
                return

            if count >= m:  # valid pattern length
                patterns += 1

            # next move
            for next in range(1, 10):
                if move_valid(digit, next):
                    visited.add(next)
                    backtrack(next, count + 1)
                    visited.remove(next)

        for d in range(1, 10):
            visited.add(d)
            backtrack(d, 1)
            visited.remove(d)

        return patterns
