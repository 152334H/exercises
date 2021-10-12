# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Either use the best diameter from the two subtrees,
        # Or use the height of the two subtrees + 0/1/2
        # Height is stored by adding it as an attribute to TreeNode
        if root.left is None and root.right is None: # leaf
            root.height = 0
            return 0
        elif root.left is None or root.right is None: # one side
            thing = root.left or root.right
            ma = self.diameterOfBinaryTree(thing)
            root.height = thing.height + 1
            if root.height > ma: ma = root.height
            return ma
        else: # both sides
            ma = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
            root.height = max(root.left.height, root.right.height) + 1
            if root.left.height + root.right.height + 2 > ma:
                ma = root.left.height + root.right.height + 2
            return ma

cases = [(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)), 3),
        (TreeNode(1, TreeNode(2)),1),
        (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3))),2)]
for t,v in cases:
    o = Solution()
    assert o.diameterOfBinaryTree(t) == v
