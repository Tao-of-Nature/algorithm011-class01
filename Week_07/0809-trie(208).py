class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end = '##'

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_node = self.root
        for c in word:
            current_node = current_node.setdefault(c, {})
        current_node[self.end] = self.end

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_node = self.root
        for c in word:
            if c not in current_node:
                return False
            current_node = current_node[c]
        return self.end in current_node


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_node = self.root
        for c in prefix:
            if c not in current_node:
                return False
            current_node = current_node[c]
        return True
