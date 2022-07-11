# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def rightSide(node,levl):
            if node:
                if len(res)==levl:
                    res.append(node.val)
                rightSide(node.right,levl+1)
                rightSide(node.left,levl+1)
            return
        res=[]
        rightSide(root,0)
        return res
            
        
        