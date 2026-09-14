# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        # Step 1: Calculate the total sum of the entire tree
        def get_total_sum(node):
            if not node:
                return 0
            return node.val + get_total_sum(node.left) + get_total_sum(node.right)
        
        total_sum = get_total_sum(root)
        self.max_prod = 0

        # Step 2: Compute subtree sums and evaluate product at each subtree root
        def get_subtree_sum(node):
            if not node:
                return 0
            
            current_sum = node.val + get_subtree_sum(node.left) + get_subtree_sum(node.right)
            
            # Calculate product if we split above this subtree
            current_product = current_sum * (total_sum - current_sum)
            self.max_prod = max(self.max_prod, current_product)
            
            return current_sum

        get_subtree_sum(root)
        
        return self.max_prod % (10**9 + 7)