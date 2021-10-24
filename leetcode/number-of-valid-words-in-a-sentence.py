from re import findall
def valid(w:str): # really really ugly solution
    if findall('[0-9]+', w): return False
    if any(c in w[:-1] for c in '!.,'): return False
    if w[-1] in '!.,': w = w[:-1]
    if len(w) == 0: return True
    if w[0] == '-' or w[-1] == '-': return False
    if w.count('-') > 1: return False
    return True
class Solution:
    def countValidWords(self, sentence: str) -> int:
        tokens = sentence.split()
        return len(list(filter(valid, tokens)))
s = Solution()
for sen in ["a", "cat and  dog", "!",
        "!this  1-s b8d!",
        "alice and  bob are playing stone-game10",
        "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."]:
    print(s.countValidWords(sen))
