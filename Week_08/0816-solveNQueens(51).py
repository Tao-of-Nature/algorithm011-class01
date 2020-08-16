class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def dfs(queens, pie, na):
            row = len(queens)
            if row == n:
                res.append(queens)
                return
            for i in range(n):
                if i not in queens and i + row not in pie and i - row not in na:
                    dfs(queens + [i], pie + [i + row], na + [i - row])

        res = []
        dfs([], [], [])
        return [['.' * pos + 'Q' + '.' * (n - 1 - pos) for pos in tmp] for tmp in res]