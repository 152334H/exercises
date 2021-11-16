class LinkedNode: # probably going to TLE from cache misses.
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = next
        self.prev = prev

# I was _fairly_ close to the actual solution,
# having realised it required doubly-linked lists,
# but I got pulled away to do something else in the last hour :(
for t in range(int(input())):
    n = int(input())
    head = LinkedNode(None)
    ptr = head
    for b in input().strip().encode():
        ptr.next = LinkedNode(b-ord('0'), ptr)
        ptr = ptr.next
    # head is a fakenode
    while 1:
        found_overall = False
        for l in range(10):
            found = False
            ptr = head.next
            while ptr.next is not None:
                if ptr.value == l and ptr.next.value == (l+1)%10:
                    found = True
                    ptr.prev.next = ptr.next
                    ptr.next.prev = ptr.prev
                    ptr.next.value = (ptr.next.value+1)%10
                ptr = ptr.next
            if found: found_overall = True
        if not found_overall:break
    s = []
    while head.next is not None:
        s.append(chr(head.next.value+ord('0')))
        head = head.next
    print('Case #{}: {}'.format(t+1, ''.join(s)))
