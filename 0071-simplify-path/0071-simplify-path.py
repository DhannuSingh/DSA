class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        components = path.split('/')
        
        for portion in components:
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion and portion != ".":
                stack.append(portion)
                
        return "/" + "/".join(stack)
