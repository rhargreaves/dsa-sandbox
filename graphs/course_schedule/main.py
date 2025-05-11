from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        courses = defaultdict(lambda: [])
        for course, req in prerequisites:
            courses[course].append(req)

        visited = set()

        def dfs(course):
            if len(courses[course]) == 0:
                return True  # course has no prerequisites

            if course in visited:
                return False  # been here before without resolution (cyclic)

            visited.add(course)
            for p in courses[course]:
                if not dfs(p):
                    return False

            visited.remove(course)  # no cyclic pre-reqs
            courses[course] = []  # optimisation do not check already "cleared" pre-reqs
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
