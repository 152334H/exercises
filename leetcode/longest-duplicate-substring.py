from collections import Counter
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        '''binsearch for the longest substring that is a duplicate.
        Check if a duplicate substring of length `mid` exists by using
        collections.Counter().'''
        lo,hi = 1,len(s)-1 # lo: substr is at least this long
        while lo < hi:
            mid = (lo+hi+1)//2 # 
            substr, freq = Counter(s[j:mid+j] for j in range(len(s)-mid+1)).most_common(1)[0]
            if freq > 1: # there is a duplicate
                lo = mid
            else: hi = mid-1
        substr, freq = Counter(s[j:lo+j] for j in range(len(s)-lo+1)).most_common(1)[0]
        return substr if freq > 1 else ""
                
s = Solution()
for (inp,out) in [
        ('banana', 3),
        ('abcd', 0),
        ("zxcvdqkfawuytt", 1),
        ("nyvzwttxsshphczjjklqniaztccdrawueylaelkqtjtxdvutsewhghcmoxlvqjktgawwgpytuvoepnyfbdywpmmfukoslqvdrkuokxcexwugogcwvsuhcziwuwzfktjlhbiuhkxcreqrdbj", 3),
    ]:
    dup = s.longestDupSubstring(inp)
    print(dup)
    assert dup in inp
    assert len(dup) == out
