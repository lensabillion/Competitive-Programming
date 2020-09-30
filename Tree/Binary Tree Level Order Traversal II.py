# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return 
        r = []
        q =[root]
        while q:
            ans =[]
            for i in range(len(q)):
                curr = q.pop(0)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                ans.append(curr.val)
           
            r.insert(0,ans)
        return r
        

                
            
