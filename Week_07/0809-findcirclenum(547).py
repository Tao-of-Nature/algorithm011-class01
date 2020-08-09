class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        def _dfs(i):
            for j in range(len(M)):
                if M[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    _dfs(j)
            return

        visited = [0 for _ in range(len(M))]
        res = 0
        for i in range(len(M)):
            if visited[i] == 0:
                visited[i] = 1
                _dfs(i)
                res += 1
        return res