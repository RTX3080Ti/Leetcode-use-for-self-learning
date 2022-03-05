class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        merged = []
        merged.append(intervals[0])
        for i in range(1, len(intervals)):
            if merged[-1][1] < intervals[i][0]:
                merged.append(intervals[i])
            else:
                if intervals[i][1] > merged[-1][1]:
                    merged[-1][1] = intervals[i][1]

        return merged

intervals = [[1,5]]
newInterval = [2,7]
s = Solution()
print(s.insert(intervals, newInterval))