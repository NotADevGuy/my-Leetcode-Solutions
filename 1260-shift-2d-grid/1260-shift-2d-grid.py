class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        from copy import deepcopy
        gridCopy = deepcopy(grid)
        for iter in range(k):
            for i in range(len(grid)):
                for j in range(1, len(grid[0])):
                    # print(i, x)
                    grid[i][j] = gridCopy[i][j - 1]
                if i != 0:
                    grid[i][0] = gridCopy[i - 1][-1]
            grid[0][0] = gridCopy[-1][-1]
            gridCopy = deepcopy(grid)
        return grid