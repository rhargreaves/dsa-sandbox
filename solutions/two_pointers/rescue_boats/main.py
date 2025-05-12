from typing import List

# 881. Boats to Save People (medium)
# https://leetcode.com/problems/boats-to-save-people/


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)

        i = 0
        j = len(people) - 1
        boats = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                j -= 1
            i += 1
            boats += 1

        return boats
