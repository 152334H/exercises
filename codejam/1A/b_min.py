from itertools import *
from operator import *
from collections import *
dd,ctr = defaultdict, Counter

_pow = pow
from math import *
pow = _pow # math's pow() doesn't provide the `mod` optional arg

from re import findall
from functools import reduce, lru_cache, singledispatchmethod

# non-generator versions of common funcs
Map = lambda f,it: list(map(f,it))
Filter = lambda f,it: list(filter(f,it))
Reversed = lambda ls: list(reversed(ls))
Zip = lambda *ls: list(zip(*ls))

from dataclasses import dataclass
from typing import List

Partition = List[List[int]]


@dataclass
class PartitioningResult:
    """The result of performing a partitioning.
    Parameters
    ----------
    partition:
        The partition as a list of lists; each inner list is a part; a subset of the
        numbers being partitioned so that their disjoint union make up the full set.
    sizes:
        List containing the corresponding sums of the parts; that is, the i'th element
        is the sum of the i'th element of the partition.
    """

    partition: Partition
    sizes: List[int]
import heapq
from itertools import count
from typing import List, Tuple

def karmarkar_karp(
    numbers: List[int],
    num_parts: int = 2,
    return_indices: bool = False,
    method: str = "purepython",
) -> PartitioningResult:
    """Produce a partition using the Karmarkar--Karp algorithm.
    Parameters
    ----------
    numbers
        The list of numbers to be partitioned.
    num_parts
        The desired number of parts in the partition. Default: 2.
    return_indices
        If True, the elements of the parts are the indices of the corresponding entries
        of numbers; if False (default), the elements are the numbers themselves.
    method
        Which specific implementation to use. Currently the only allowed (and default)
        value is "purepython".
    Returns
    -------
    A partition representing by a ``PartitioningResult``.
    """
    if method not in METHODS:
        raise ValueError(
            f'Invalid method "{method}". Valid options: {", ".join(METHODS)}'
        )
    return METHODS[method](numbers, return_indices, num_parts)


def _argsort(seq: List[int]) -> List[int]:
    return sorted(range(len(seq)), key=seq.__getitem__)


def _karmarkar_karp_pure_python(
    numbers: List[int], return_indices: bool, num_parts: int
) -> PartitioningResult:
    partitions: List[Tuple[int, int, Partition, List[int]]] = []
    heap_count = count()  # To avoid ambiguity in heap
    for i in range(len(numbers)):
        this_partition: Partition = []
        for n in range(num_parts - 1):
            this_partition.append([])
        this_partition.append([i if return_indices else numbers[i]])
        this_sizes: List[int] = [0] * (num_parts - 1) + [numbers[i]]
        heapq.heappush(
            partitions, (-numbers[i], next(heap_count), this_partition, this_sizes)
        )
    for k in range(len(numbers) - 1):
        _, _, p1, p1_sum = heapq.heappop(partitions)
        _, _, p2, p2_sum = heapq.heappop(partitions)
        new_sizes: List[int] = [
            p1_sum[j] + p2_sum[num_parts - j - 1] for j in range(num_parts)
        ]
        new_partition: Partition = [
            p1[j] + p2[num_parts - j - 1] for j in range(num_parts)
        ]
        indices = _argsort(new_sizes)
        new_sizes = [new_sizes[i] for i in indices]
        new_partition = [new_partition[i] for i in indices]
        diff = new_sizes[-1] - new_sizes[0]
        heapq.heappush(partitions, (-diff, next(heap_count), new_partition, new_sizes))
    _, _, final_partition, final_sums = partitions[0]
    return PartitioningResult(final_partition, final_sums)

METHODS = {"purepython": _karmarkar_karp_pure_python}

# for the package
from typing import *
from sys import stdout
from random import randint

def printf(*args, **kwargs):
    print(*args, **kwargs)
    stdout.flush()

def canPartition(nums: List[int]) -> bool:
    s = sum(nums)
    if s % 2 != 0: return False
    s //= 2
    dp = dd(lambda: False, {0: True})
    possible = {0:()}
    for num in nums:
        for i in range(s, num-1, -1):
            if not dp[i] and dp[i-num]:
                possible[i] = possible[i-num] + (num,)
            dp[i] = dp[i] or dp[i-num]
    return dp[s],possible[s]

for t in range(int(input())):
    n = 100; assert int(input()) == 100
    nums = []
    for b in range(5,30):
        v = 1<<b
        nums += [v-1,v,v+1,v+2]

    print(' '.join(map(str, nums)))
    newNums = Map(int, input().split())
    #newNums = list(randint(1,10**9) for _ in range(n))
    if sum(newNums+nums) % 2 != 0: newNums[0]+=1
    res = karmarkar_karp(nums+newNums, num_parts=2).partition
    #print(sum(res[0]), sum(res[1]))
    printf(' '.join(map(str,res[0])))
