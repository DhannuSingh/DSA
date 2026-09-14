# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        stack = []
        i = 0
        n = len(traversal)
        
        while i < n:
            # Step 1: Count the number of dashes to determine depth
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            
            # Step 2: Read the node's numerical value
            val = 0
            while i < n and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1
            
            node = TreeNode(val)
            
            # Step 3: Pop stack until length equals current node's depth
            while len(stack) > depth:
                stack.pop()
            
            # Step 4: Attach to parent
            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            
            # Step 5: Push current node onto stack
            stack.append(node)
        
        # The root is the first node pushed to the stack
        return stack[0]