#!/usr/bin/env python3.8
from collections import Counter
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count = 0
        for i in range(len(word)):
            for j in range(i+1,len(word)+1):
                ctr = Counter(word[i:j])
                if all(c in ctr for c in 'aeiou') and len(ctr) == 5:
                    count += 1
        return count
        
s = Solution()
for inp,out in [
        ('aeiouu', 2),
        ('unicornarihan', 0),
        ('cuaieuouac', 7),
        ('bbaeixoubb', 0)
    ]:
    res = s.countVowelSubstrings(inp)
    print(inp,out)
    assert res == out

