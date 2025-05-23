class TrieNode:
    # INIT FUNCTION
    def __init__(self):
        self.children={}
        self.end_of_word=False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Time complex o(m) m: Word characters
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.end_of_word=True

    def search(self, word: str) -> bool:
        # Time complex o(m) m: Word characters
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        if current.end_of_word==True:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        # Time complex o(m) m: Word characters
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)