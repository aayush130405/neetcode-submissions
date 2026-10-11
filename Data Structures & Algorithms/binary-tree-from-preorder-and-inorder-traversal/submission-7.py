# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_index = 0
        inorder_map = {val: index for index, val in enumerate(inorder)}
        def build(left, right):
            nonlocal pre_index
            if left > right:
                return None
            node_val = preorder[pre_index]
            node = TreeNode(node_val)
            pre_index += 1
            in_index = inorder_map[node_val]
            node.left = build(left, in_index - 1)
            node.right = build(in_index + 1, right)
            return node
        return build(0, len(inorder) - 1)