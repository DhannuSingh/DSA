# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if not root:
            return None
        
        # If node value is less than low, left subtree is also out of range
        if root.val < low:
            return self.trimBST(root.right, low, high)
        
        # If node value is greater than high, right subtree is also out of range
        if root.val > high:
            return self.trimBST(root.left, low, high)
        
        # Node value is within [low, high], process both children
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        return root