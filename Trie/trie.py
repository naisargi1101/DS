class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # O(N) N=length of string
    def insert(self, word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.isEndOfWord = True
    
    # O(N) N=length of string
    def search(self, word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return curr.isEndOfWord
    
    def startsWith(self, word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return True

obj = Trie()
obj.insert("word")
param_2 = obj.search("word")
param_3 = obj.startsWith("pre")
print(param_2, param_3)