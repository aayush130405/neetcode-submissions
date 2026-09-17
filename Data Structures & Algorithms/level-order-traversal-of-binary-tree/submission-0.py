# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        result = []
        if root is None:
            return []
        q = deque()
        q.append(root)
        while q:
            level_size = len(q)
            current_level = []
            for _ in range(level_size):
                node = q.popleft()
                current_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(current_level)
        return result
        