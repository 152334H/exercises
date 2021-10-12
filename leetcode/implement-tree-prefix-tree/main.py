# Original inspiration for rust solution. Code is somewhat dirty with repeated lines.
class Edge(str): pass
class Trie:
    def __init__(self): self.edges = {} # char:Edge
    def addleaf(self): self.edges[""] = Trie()
    def addedge(self, word: str, addnull: bool=True) -> None:
        self.edges[word[0]] = Edge(word)
        t = self.edges[word[0]].target = Trie()
        if addnull: t.addleaf()
    def findEdge(self, word: str):
        if word == "": return None
        c = word[0]
        if c not in self.edges: return None
        substr = self.edges[c]
        if substr != word[:len(substr)]: return None
        return substr
    def insert(self, word: str) -> None:
        if not word: # word is ""
            self.addleaf()
            return
        c = word[0]
        substr = self.edges.get(c, None)
        if substr is not None:
            if len(substr) <= len(word) and substr == word[:len(substr)]: # edge matches fully
                substr.target.insert(word[len(substr):])
            else: # we need to split the edge
                try: # within this block, both substr and word are long enough
                    diffi = next(i for i,t in enumerate(zip(substr,word)) if t[0] != t[1])
                except StopIteration: # word is shorter than substr
                    diffi = len(word)
                SUBSTR_IS_LONGER = diffi == len(word)
                old_trie = self.edges[c]
                self.addedge(word[:diffi], addnull=SUBSTR_IS_LONGER) # the split happens where a word does not exist.
                subsubstr = Edge(substr[diffi:])
                self.edges[c].target.edges[subsubstr[0]] = subsubstr
                subsubstr.target = old_trie.target
                if not SUBSTR_IS_LONGER: self.edges[c].target.addedge(word[diffi:])

        else: # a completely new substr
            self.addedge(word)

    def search(self, word: str) -> bool:
        if word == "": return "" in self.edges
        substr = self.findEdge(word)
        return False if substr is None else substr.target.search(word[len(substr):])

    def startsWith(self, prefix: str) -> bool:
        if prefix == "": return True
        c = prefix[0]
        if c not in self.edges: return False
        substr = self.edges[c]
        if len(substr) > len(prefix): return substr[:len(prefix)] == prefix
        if substr != prefix[:len(substr)]: return False
        return substr.target.startsWith(prefix[len(substr):])
        


# Your Trie object will be instantiated and called as such:

obj = Trie()
obj.insert("apple")
assert obj.search("apple")
assert not obj.search("app")
assert obj.startsWith("app")
obj.insert("app")
assert obj.search("app")
print(obj)
print(obj.edges)
print(obj.edges['a'])
print(obj.edges['a'].target)
print(obj.edges['a'].target.edges)
print(obj.edges['a'].target.edges['l'])
print(obj.edges['a'].target.edges['l'].target)
print(obj.edges['a'].target.edges['l'].target.edges)
