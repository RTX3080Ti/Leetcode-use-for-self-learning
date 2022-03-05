class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == None or len(grid) == 0:
            return 0

        num = 0
        row = len(grid)
        col = len(grid[0])
        union = []
        used = []
        for k in range(row * col):
            union.append(k)
            used.append(0)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" or union[i * col + j] != i * col + j:
                    if i + 1 <= row-1:
                        if grid[i + 1][j] == "1" and used[(i + 1) * col + j] == 0:
                            union[(i + 1) * col + j] = union[i * col + j]
                            used[(i + 1) * col + j] = 1
                    if j + 1 <= col-1:
                        if grid[i][j + 1] == "1" and used[i * col + j + 1] == 0:
                            union[i * col + j + 1] = union[i * col + j]
                            used[i * col + j + 1] = 1
                    if i-1 >= 0:
                        if grid[i - 1][j] == "1" and used[(i - 1) * col + j] == 0:
                            union[(i - 1) * col + j] = union[i * col + j]
                            used[(i - 1) * col + j] = 1
                    if j-1 >= 0:
                        if grid[i][j - 1] == "1" and used[i * col + j - 1] == 0:
                            union[i * col + j - 1] = union[i * col + j]
                            used[i * col + j - 1] = 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and union[i * col + j] == i * col + j:
                    num += 1
        print(union)
        return  num

grid = [["1","1","1","1","1","0","1","1","1","1"],
        ["1","0","1","0","1","1","1","1","1","1"],
        ["0","1","1","1","0","1","1","1","1","1"],
        ["1","1","0","1","1","0","0","0","0","1"],
        ["1","0","1","0","1","0","0","1","0","1"],
        ["1","0","0","1","1","1","0","1","0","0"],
        ["0","0","1","0","0","1","1","1","1","0"],
        ["1","0","1","1","1","0","0","1","1","1"],
        ["1","1","1","1","1","1","1","1","0","1"],
        ["1","0","1","1","1","1","1","1","1","0"]]

s = Solution()
print(s.numIslands(grid))