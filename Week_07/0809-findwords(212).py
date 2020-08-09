class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def _dfs(i, j, node, word_tmp):

            char = board[i][j]
            if char not in node: return

            node = node[char]
            word_tmp += char

            if END_LABEL in node:
                if word_tmp not in res:
                    res.append(word_tmp)

            board[i][j] = '$'
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                tmp_i = i + dx
                tmp_j = j + dy
                if 0 <= tmp_i < row_len and 0 <= tmp_j < col_len and board[tmp_i][tmp_j] in node:
                    _dfs(tmp_i, tmp_j, node, word_tmp)
            board[i][j] = char
            
            return
                
        if not board: return []

        res = []
        trie_cache = {}
        END_LABEL = '#'

        for word in words:
            node = trie_cache
            for char in word:
                node = node.setdefault(char, {})
            node[END_LABEL] = END_LABEL
        
        row_len = len(board)
        col_len = len(board[0])
        for i in range(row_len):
            for j in range(col_len):
                _dfs(i, j, trie_cache, '')
        return res