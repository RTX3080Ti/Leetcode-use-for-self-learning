class UnionFind(object):
    def __init__(self, grid):
        row = len(grid)
        col = len(grid[0])
        self.root = [-1] * (row * col)
        self.cnt = row * col
        for i in range(0, row*col):
            self.root[i] = i

    def find(self, x):
        if x == self.root[x]:
            return self.root[x]
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def union(self, x, y):
        if self.find(x) != self.find(y):
            self.root[self.root[x]] = self.root[y]
            self.cnt -= 1

    def getCnt(self):
        return self.cnt

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0:
            return 0
        row = len(grid)
        col = len(grid[0])
        waters = 0
        uf = UnionFind(grid)
        for i in range(0, row):
            for j in range(0, col):
                if grid[i][j] == '0':
                    waters += 1
                else:
                    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
                    for x, y in directions:
                        x = x + i
                        y = y + j
                        if x >= 0 and y >= 0 and x < row and y < col and grid[x][y] == '1':
                            uf.union(x * col + y, i * col + j)
        return uf.getCnt() - waters

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
s = Solution()
print(s.numIslands(grid))