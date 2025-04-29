from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        summed_xors = 0

        def xor_nums(index, current_set):
            nonlocal summed_xors

            # Base case: we've made yes/no decisions for all numbers
            # Now we process whatever subset we built
            if index == len(nums):
                result = 0
                for n in current_set:
                    result ^= n
                summed_xors += result
                return

            # Decision 1: Skip current number
            # Try building subsets without nums[index]
            xor_nums(index + 1, current_set)
            # Automatic backtrack happens here!

            # Decision 2: Include current number
            current_set.append(nums[index])  # Add nums[index] to our subset
            xor_nums(index + 1, current_set)  # Try building subsets with nums[index]
            current_set.pop()  # Backtrack: remove nums[index]

        # Start with empty set, index 0
        xor_nums(0, [])
        return summed_xors


# For nums = [1,3]:
#                        (index=0, set=[])
#                       /                  \
#            (index=1, [])              (index=1, [1])
#            /           \              /            \
# (index=2, [])    (index=2, [3])   (index=2, [1])  (index=2, [1,3])
#     ⬇️              ⬇️               ⬇️              ⬇️
# BASE CASE!      BASE CASE!        BASE CASE!      BASE CASE!
# XOR=0          XOR=3             XOR=1           XOR=2
