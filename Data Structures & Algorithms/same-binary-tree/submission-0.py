# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False

        s1 = [p]
        s2 = [q]

        while s1 and s2:
            node1 = s1.pop()
            node2 = s2.pop()

            if node1 is None and node2 is not None:
                return False
            if node1 is not None and node2 is None:
                return False
            if node1 is None and node2 is None:
                continue
            if node1.val != node2.val:
                return False

            if node1.right:
                s1.append(node1.right)
            else:
                s1.append(None)
            if node1.left:
                s1.append(node1.left)
            else:
                s1.append(None)
            if node2.right:
                s2.append(node2.right)
            else:
                s2.append(None)
            if node2.left:
                s2.append(node2.left)
            else:
                s2.append(None)
        return True