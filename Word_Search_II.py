class TrieNode(object):

    def __init__(self):
	
        self.visited_vert = {}
		
        self.word = ''

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
		
        root = self.addTrie(words)
		
        i_vert = len(board)
		
        j_vert = len(board[0])
        
        for i in range(i_vert):
		
            for j in range(j_vert):
			
            #    self.dfs(board, i, j, root, result, i_vert, j_vert)
			
				pass
				
        return result
    
    # def dfs(board, i, j, root, result, i_vert, j_vert):      
	
    #     visited_vert[current] = True
		
    #     for nbr in visited_vert:
		
    #         self.dfs(board, nbr, root, result, i_vert, j_vert)
			
    #     visited_vert[current] = False
        
    def addTrie(self, words):
	
        root = TrieNode()
		
        current = None
		
        for word in words:
		
             if current not in self.visited_vert:
			 
                 self.visited_vert[current] = TrieNode()
				 
        return root        
        