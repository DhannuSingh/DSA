# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_vals = []
        
        # Step 1: Collect node values in sorted order using In-Order traversal
        def in_order(node):
            if not node:
                return
            in_order(node.left)
            sorted_vals.append(node.val)
            in_order(node.right)
            
        in_order(root)
        
        # Step 2: Build height-balanced BST from sorted array
        def build_balanced_bst(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            root_node = TreeNode(sorted_vals[mid])
            
            root_node.left = build_balanced_bst(left, mid - 1)
            root_node.right = build_balanced_bst(mid + 1, right)
            
            return root_node
        
        return build_balanced_bst(0, len(sorted_vals) - 1)