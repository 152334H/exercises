from typing import List
from itertools import chain, combinations
from collections import defaultdict as dd
class Solution:
    def possibleHashes(self, puzzle: str):
        '''get the powerset of the puzzle,
        ignoring all subsets that don't contain puzzle[0]'''
        first,*truncuated = puzzle
        # 64 possibilities here, maximally.
        # sorting a length 7 tuple * 64 possibilities.
        return (tuple(sorted((first,)+h)) for h in 
                    chain.from_iterable(combinations(truncuated,r)
                         for r in range(len(puzzle)+1)
                    ) # 64 possibilities here, maximally
               ) # runtime of sorting a 7 element tuple * 64
    
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        hash_lookup = dd(list)
        # O(k * puzzles.length)
        for i,p in enumerate(puzzles):
            for h in self.possibleHashes(p): # O(2**puzzles[i].length),
                hash_lookup[h].append(i) # which is essentially O(k)

        res = [0 for _ in range(len(puzzles))]
        # O(words[i].length*words.length + sum(res))
        for w in words:
            # this step is approximately O(words[i].length) per loop
            alphabet = tuple(sorted(set(w)))
            # this step, counting all loops, is O(sum(res))
            for i in hash_lookup[alphabet]: res[i] += 1
        return res
        ''' O(words[i].length*8*words.length*puzzles.length) ~= 10**11
        return [sum(
                any(c == p[0] for c in w) and all(c in p for c in w)
                for w in words
            ) for p in puzzles]
        '''
    


s = Solution()
for (words, puzzles, out) in [
        (["aaaa","asas","able","ability","actt","actor","access"],
        ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"],
        [1,1,3,2,4,0]),

        (["apple","pleas","please"],
        ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"],
        [0,1,3,2,0])
    ]:
    res = s.findNumOfValidWords(words,puzzles)
    print(res,out)
    assert res == out
