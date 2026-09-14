# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None and subRoot is not None:
            return False
        if subRoot is None and root is not None:
            return False
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                #found start of subtree
                is_same = True
                compare_stack = [(node, subRoot)]
                while compare_stack:
                    node1, node2 = compare_stack.pop()
                    if node1 is None and node2 is None:
                        continue
                    if node1 is None or node2 is None:
                        is_same = False
                        break
                    if node2.val != node1.val:
                        is_same = False
                        break
                    compare_stack.append((node1.left, node2.left))
                    compare_stack.append((node1.right, node2.right))
                if is_same:
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False