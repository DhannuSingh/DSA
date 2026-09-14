# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        queue = [root]
        level = 0
        
        while queue:
            level_size = len(queue)
            # Set prev threshold based on level parity
            prev = float('-inf') if level % 2 == 0 else float('inf')
            
            for _ in range(level_size):
                node = queue.pop(0)
                val = node.val
                
                # Even level checks: values must be ODD and STRICTLY INCREASING
                if level % 2 == 0:
                    if val % 2 == 0 or val <= prev:
                        return False
                # Odd level checks: values must be EVEN and STRICTLY DECREASING
                else:
                    if val % 2 != 0 or val >= prev:
                        return False
                
                prev = val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level += 1
            
        return True