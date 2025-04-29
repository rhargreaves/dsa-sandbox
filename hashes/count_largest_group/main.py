from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:

        def sumDigits(i):
            return sum([int(d) for d in str(i)])

        freqs = defaultdict(lambda: 0)
        max_freq = 0
        for i in range(1, n + 1):
            s = sumDigits(i)
            freqs[s] += 1
            max_freq = max(freqs[s], max_freq)

        freq_counts = defaultdict(lambda: 0)
        for k, v in freqs.items():
            freq_counts[v] += 1

        return freq_counts[max_freq]
