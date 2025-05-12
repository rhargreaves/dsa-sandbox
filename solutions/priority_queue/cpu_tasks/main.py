import heapq
from typing import List

# 1834. Single-Threaded CPU
# https://leetcode.com/problems/single-threaded-cpu/


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        # remember original index before sorting
        for i, t in enumerate(tasks):
            t.append(i)

        # sort by enqueued time
        tasks.sort(key=lambda t: t[0])

        q = []
        cur_time = 0
        res = []
        task_index = 0

        # while we still have tasks to process
        while len(res) < len(tasks):

            # add any tasks that are schedulable now
            while task_index < len(tasks) and tasks[task_index][0] <= cur_time:
                proc_time = tasks[task_index][1]
                orig_id = tasks[task_index][2]
                heapq.heappush(
                    q, (proc_time, orig_id)
                )  # include orig_id here as tie-breaker
                task_index += 1

            # if no tasks schedulable, warp time to the next queued task time
            if not q and task_index < len(tasks):
                cur_time = tasks[task_index][0]
                continue

            # process only one!
            # we might have smaller tasks that can now be executed by the shifting time
            if q:
                proc_time, orig_id = heapq.heappop(q)
                cur_time += proc_time
                res.append(orig_id)

        return res
