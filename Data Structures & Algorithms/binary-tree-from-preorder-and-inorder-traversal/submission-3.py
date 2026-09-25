# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_index = 0
        inorder_map = {value: index for index, value in enumerate(inorder)}
        def build(left, right):
            nonlocal preorder_index
            if left > right:
                return None
            root_val = preorder[preorder_index]
            root = TreeNode(root_val)

            preorder_index += 1

            inorder_index = inorder_map[root.val] #
            
            root.left = build(left, inorder_index - 1)
            root.right = build(inorder_index + 1, right)

            return root
        return build(0, len(inorder) - 1)

