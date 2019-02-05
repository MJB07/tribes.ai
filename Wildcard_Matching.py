class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        string, pattern = len(s), len(p)
        
        result_s, result_p = None,None
        
        s_i = p_i = 0
        
        while s_i < string:
            
            if p_i < pattern and (p[p_i] == "?" or s[s_i] == p[p_i]):
                
                s_i += 1
                
                p_i += 1
                
            elif p_i < pattern and p[p_i] == "*":
                
                result_s, result_p = s_i, p_i
                
                p_i += 1
                
            elif result_p is not None:
                
                s_i, p_i = result_s + 1, result_p
                
            else:
                return False        
            
        while p_i < pattern:
            
            if p[p_i] != "*":
                
                return False
            
            p_i += 1
            
        return True            