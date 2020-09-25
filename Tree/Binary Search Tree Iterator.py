# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        def helper(root):
            if root:
                helper(root.right)
                self.stack.append(root.val)
                helper(root.left)
            return self.stack
        self.stackMain = helper(root)
        

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        
        small = self.stackMain.pop()
        return small
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if len(self.stackMain) > 0:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
