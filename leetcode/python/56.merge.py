from typing import List


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        index = 0
        while index < len(intervals) - 1:
            if intervals[index][1] < intervals[index + 1][0]:
                index += 1
            else:
                intervals[index][1] = max(intervals[index][1], intervals[index + 1][1])
                del intervals[index + 1]
        return intervals