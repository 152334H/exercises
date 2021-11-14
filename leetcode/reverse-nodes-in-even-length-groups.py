from typing import List,Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        prev = None # prev will never be None when relevant.
        for i in range(1,10**6): # max is 10**5.
            nodes = [] # collect the nodes in this group.
            for _ in range(i):
                if ptr is None: break
                nodes.append(ptr)
                ptr = ptr.next
            # now handle the two cases
            if len(nodes) % 2: # just move forward
                prev = nodes[-1]
            else: # reverse the next i nodes
                for n in nodes[::-1]:
                    prev.next = n
                    prev = n
                prev.next = ptr
            # exit if needed
            if ptr is None: break
        return head # this never changes

s = Solution()
for (inp,out) in [
        ([5,2,6,3,9,1,7,3,8,4], [5,6,2,3,9,1,4,8,3,7]),
        ([1,1,0,6],[1,0,1,6]),
        ([2,1],[2,1]),
        ([8],[8]),
        ([0,4,2,1,3], [0,2,4,3,1])
    ]:
    head = ListNode(inp[0])
    ptr = head
    for i in inp[1:]:
        ptr.next = ListNode(i)
        ptr = ptr.next
    res = s.reverseEvenLengthGroups(head)

    ptr = res
    for i in out:
        print(ptr.val,i)
        assert ptr.val == i
        ptr = ptr.next
    assert ptr is None
    print('---')


