# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subtree_counts = collections.defaultdict(int)
        result = []

        def serialize(node):
            if not node:
                return "#"
            
            # Post-order serialization: root + left + right
            key = f"{node.val},{serialize(node.left)},{serialize(node.right)}"
            
            # Increment frequency count
            subtree_counts[key] += 1
            
            # Add to result only when duplicate is first detected
            if subtree_counts[key] == 2:
                result.append(node)
                
            return key

        serialize(root)
        return result