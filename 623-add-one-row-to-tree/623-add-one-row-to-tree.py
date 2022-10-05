# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(node,h,dr):
            if h==depth:
                temp=TreeNode(val)
                if dr==0:
                    temp.left=node
                else:
                    temp.right=node
                return temp
            if not node:
                return node
            node.left=dfs(node.left,h+1,0)
            node.right=dfs(node.right,h+1,1)
            return node
        return dfs(root,1,0)
            
            
        