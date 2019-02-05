# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def maxPathSum(self, root) -> 'int':
        """
        :type root: TreeNode
        :rtype: int
        """
                
        self.max_value = float("-inf")
        
        self.maxPathResult(root)
        
        return self.max_value
    
    
    def maxPathResult(self, root) -> 'int':
        
        if root == None:
            
             return 0
            
        l_sum = self.maxPathResult(root.left)
        
        r_sum = self.maxPathResult(root.right)
        
        if l_sum < 0 and r_sum < 0:
            
            self.max_value = max(self.max_value, root.val)
            
            return root.val
        
        if l_sum > 0 and r_sum > 0:
            
            self.max_value = max(self.max_value, root.val + l_sum + r_sum)
            
        maxFnl = max(l_sum, r_sum) + root.val
        
        self.max_value = max(self.max_value, maxFnl)
        
        return maxFnl        