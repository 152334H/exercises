#!/usr/bin/env python3.8
from collections import deque,defaultdict as dd
from typing import List,Optional
# Definition for a binary tree node.

class Solution:
    def countVowels(self, word: str) -> int:
        res = 0
        for i,c in enumerate(word):
            if c in 'aeiou':
                max_min = min(i+1,len(word)-i)
                dupes = len(word)-max_min*2
                res += max_min*dupes + (max_min+1)*max_min
                ''' unoptimised:
                for j in range(1,len(word)+1):
                    min_dist = min(i+1,j,len(word)-i,len(word)-j+1)
                    res += min_dist
                '''
        return res
        '''attempt 1:
        sat = [0]
        for i in word: sat.append(sat[-1]+(i in 'aeiou'))
        res = 0
        for length in range(1,len(word)+1):
            for i in range(len(word)-length+1):
                res += sat[i+length] - sat[i]
        return res'''
        
s = Solution()
for inp,out in [
        ('aba', 6),
        ('abc', 3),
        ('ltcd', 0),
        ('noosabasboosa', 237)
    ]:
    res = s.countVowels(inp)
    print(inp,out)
    assert res == out

