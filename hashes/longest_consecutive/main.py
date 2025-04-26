from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for n in num_set:
            if n - 1 not in num_set:  # start of sequence
                cur_num = n
                cur_length = 1
                while cur_num + 1 in num_set:
                    cur_length += 1
                    cur_num += 1

                max_length = max(cur_length, max_length)

        return max_length
