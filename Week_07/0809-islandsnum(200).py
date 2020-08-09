class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or not grid[0]: return 0
        row_len = len(grid)
        col_len = len(grid[0])

        parent_line = [i for i in range(row_len * col_len)]
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(row_len):
            for j in range(col_len):
                if visited[i][j] == 0 and grid[i][j] == '1':
                    visited[i][j] = 1
                    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        tmp_i, tmp_j = i + dx, j + dy
                        if 0 <= tmp_i < row_len and 0 <= tmp_j < col_len and grid[tmp_i][tmp_j] == '1' and visited[tmp_i][tmp_j] == 0:
                            self._union(parent_line, i*col_len+j, tmp_i*col_len+tmp_j)
        res = set()                
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == '1':
                    res.add(self._parent(parent_line, i*col_len+j))
        return len(res)

    def _union(self, parent_line, i, j):
        parent_i = self._parent(parent_line, i)
        parent_j = self._parent(parent_line, j)
        parent_line[parent_i] = parent_j

    def _parent(self, parent_line, i):
        root = i
        while parent_line[root] != root:
            root = parent_line[root]
        while parent_line[i] != root:
            tmp = i
            i = parent_line[i]
            parent_line[tmp] = root
        return root