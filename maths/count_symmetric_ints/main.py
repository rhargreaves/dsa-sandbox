class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for n in range(low, high + 1):
            digits = [int(c) for c in str(n)]
            d_len = len(digits)

            if d_len % 2 == 1:
                continue

            if sum(digits[0 : (d_len // 2)]) == sum(digits[(d_len // 2) : d_len]):
                count += 1

        return count
