"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals_sorted = sorted(intervals, key=lambda v: v.start)

        for i in range(1, len(intervals)):
            curr = intervals_sorted[i]
            prev = intervals_sorted[i-1]

            if curr.start < prev.end:
                return False
        return True

