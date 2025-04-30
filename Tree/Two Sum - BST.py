def findTarget(root, k):
    vis = set()
    def solve(root):
        if root==None:
            return False
        if k-root.data in vis:
            return True
        
        vis.add(root.data)

        return solve(root.left) or solve(root.right)
    
    return solve(root)



_________________________________________________________________________________________________________



Approach 2:
Store inOrder and apply 2 pointer approach
