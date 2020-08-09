class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return []
        parent = [i for i in range(len(board)*len(board[0]))] + [len(board)*len(board[0])]
        
        def _find(i):
            root = i
            while root != parent[root]:
                root = parent[root]
            while parent[i] != root:
                tmp = i
                i = parent[i]
                parent[tmp] = root
            return root

        def _union(i, j):
            p_i = _find(i)
            p_j = _find(j)
            parent[p_i] = p_j
            return

        row_len = len(board)
        col_len = len(board[0])
        dummy_node = row_len * col_len
        for i in range(row_len):
            for j in range(col_len):
                if board[i][j] == 'O' and (i in [0, row_len-1] or j in [0, col_len-1]):
                    _union(dummy_node, i*col_len + j)
                elif board[i][j] == 'O':
                    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        tmp_i, tmp_j = i + dx, j + dy
                        if 0 <= tmp_i < row_len and 0 <= tmp_j < col_len and board[tmp_i][tmp_j] == 'O':
                            _union(i*col_len + j, tmp_i*col_len + tmp_j)

        for i in range(row_len):
            for j in range(col_len):
                if _find(dummy_node) == _find(i*col_len + j):
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        return