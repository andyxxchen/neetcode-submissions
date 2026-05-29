
# root doesn't save value, all the val should be in children dict 
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        # if next char is not in the children, add it and goto next TrieNode
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        
        # the end just a marker
        node.isWord = True

    def search(self, word: str) -> bool:
        # if any of the subWord can match return True
        def dfs(node, i):
            if i == len(word):
                return node.isWord
            
            # i means the current char should be processed
            ch = word[i]

            if ch != '.':
                if ch not in node.children:
                    return False
                node = node.children[ch]
                return dfs(node, i+1)

            else: # wildcard
                # traverse all children and do dfs
                for c in node.children.values():
                    if dfs(c, i+1):
                        return True

                return False
        
        return dfs(self.root, 0)
                
                
