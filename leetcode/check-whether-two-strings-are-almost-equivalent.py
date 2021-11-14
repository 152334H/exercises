from collections import Counter
from string import ascii_lowercase
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c1,c2 = Counter(word1),Counter(word2)
        return not any(abs(c1[c]-c2[c]) > 3 for c in ascii_lowercase)

s = Solution()
for (inp,out) in [
        (('aaaa', 'bccb'), False),
        (('abcdeef', 'abaaacc'), True),
        (('cccddabba', 'babababab'), True)
    ]:
    assert s.checkAlmostEquivalent(*inp) == out
