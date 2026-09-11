# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [(root, False)]
        diameter = 0
        mapp = {}
        while stack:
            node, visited = stack.pop()
            if visited == False:
                stack.append((node, True))

                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))
            else:
                if node.left:
                    left = mapp[node.left]
                else:
                    left = 0
                if node.right:
                    right = mapp[node.right]
                else:
                    right = 0
                
                diameter = max(diameter, left + right)
                height = 1 + max(left, right)
                mapp[node] = height
        return diameter