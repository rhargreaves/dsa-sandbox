from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:

        def sumDigits(i):
            return sum([int(d) for d in str(i)])

        freqs = defaultdict(lambda: 0)
        max_freq_count = 0
        max_freq = 0
        for i in range(1, n + 1):
            s = sumDigits(i)
            freqs[s] += 1
            if freqs[s] > max_freq:
                max_freq_count = 1
                max_freq = freqs[s]
            elif freqs[s] == max_freq:
                max_freq_count += 1

        return max_freq_count
