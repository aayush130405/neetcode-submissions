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
    def dfs(self, node, maxValue):
        if not node:
            return 0
        good = 1 if node.val >= maxValue else 0
        maxValue = max(maxValue, node.val)
        left = self.dfs(node.left, maxValue)
        right = self.dfs(node.right, maxValue)
        return good + left + right