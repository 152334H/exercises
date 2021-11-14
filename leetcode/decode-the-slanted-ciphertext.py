class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # braindead simple: convert the text to the grid,
        # then read off of the grid and strip trailing spaces.
        cols = len(encodedText) // rows
        if cols == 0 or rows == 0: return ''
        grid = [encodedText[i:i+cols] for i in range(0, len(encodedText), cols)]
        s = []
        for c in range(cols):
            for r in range(rows):
                if c+r < cols: s.append(grid[r][c+r])
        return ''.join(s).rstrip()
s = Solution()
for (inp,out) in [
    (("ch   ie   pr",3), 'cipher'),
    (("iveo    eed   l te   olc",4), "i love leetcode"),
    (('coding',1), 'coding'),
    ((' b  ac',2), ' abc'),
    (('',5), '')
    ]:
    assert s.decodeCiphertext(*inp) == out
