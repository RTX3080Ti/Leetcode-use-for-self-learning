class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        merged = []
        merged.append(intervals[0])

        for i in range(1,len(intervals)):
            if merged[-1][1] < intervals[i][0]:
                merged.append(intervals[i])
            else:
                if intervals[i][1] > merged[-1][1]:
                    merged[-1][1] = intervals[i][1]

        return merged

intervals = [[1,9],[2,5],[19,20],[10,11],[12,20],[0,3],[0,1],[0,2]]
s = Solution()
print(s.merge(intervals))