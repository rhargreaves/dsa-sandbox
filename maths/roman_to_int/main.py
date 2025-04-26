class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": (1, ["X", "V"]),
            "V": (5, []),
            "X": (10, ["L", "C"]),
            "L": (50, []),
            "C": (100, ["D", "M"]),
            "D": (500, []),
            "M": (1000, []),
        }
        total = 0
        i = len(s) - 1
        while i >= 0:
            sym = symbols[s[i]]
            if i + 1 != len(s) and s[i + 1] in sym[1]:
                total -= sym[0]
            else:
                total += sym[0]
            i -= 1

        return total
