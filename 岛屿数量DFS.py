class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid, x, y, row, col):
            if x < 0 or y < 0 or x >= row or y >= col or grid[x][y] == "0":
                return

            grid[x][y] = "0"
            dfs(grid, x+1, y, row, col)
            dfs(grid, x-1, y, row, col)
            dfs(grid, x, y+1, row, col)
            dfs(grid, x, y-1, row, col)

        if grid == None or len(grid) == 0:
            return 0
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 发现新大陆
                if grid[i][j] == "1":
                    num += 1
                    dfs(grid, i, j, len(grid), len(grid[0]))
        return  num

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

s = Solution()
print(s.numIslands(grid))