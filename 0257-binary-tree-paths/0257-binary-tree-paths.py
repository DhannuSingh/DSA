# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if not root:
            return res
        self.dfs(root, "", res)
        return res

    def dfs(self, node: TreeNode, path: str, res: List[str]) -> None:
        if not path:
            path = str(node.val)
        else:
            path += "->" + str(node.val)
            
        if not node.left and not node.right:
            res.append(path)
            return
            
        if node.left:
            self.dfs(node.left, path, res)
        if node.right:
            self.dfs(node.right, path, res)
