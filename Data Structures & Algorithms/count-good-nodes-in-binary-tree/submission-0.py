# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root, root.val)
    def dfs(self, node, maxx):
        if not node: 
            return 0
        good = 1 if node.val >= maxx else 0
        maxx = max(maxx, node.val)
        left = self.dfs(node.left, maxx)
        right = self.dfs(node.right, maxx)
        return good + left + right