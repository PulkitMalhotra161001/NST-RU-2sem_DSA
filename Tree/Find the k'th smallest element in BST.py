def kthSmallestInBST(root, k):
    elements = [] 
    def inOrder(root):
        if not root:
            return 
        
        inOrder(root.left)
        elements.append(root.data)
        inOrder(root.right)
    
    inOrder(root)
    return elements[k - 1]

________________________________________________________________________

def kthSmallestInBST(root, k): 
    count=0
    ans=0
    def inOrder(root):
        nonlocal count
        nonlocal ans

        if root==None:
            return
        
        inOrder(root.left)

        count+=1
        if count==k:
            ans = root.data

        inOrder(root.right)
    inOrder(root)
    return ans
