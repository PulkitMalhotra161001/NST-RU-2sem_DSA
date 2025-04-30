def rangeSumBST(root, low, high):
    if root==None:
        return 0

    ans=0
    if root.data>=low and root.data<=high:
        ans+=root.data
    
    ans+= rangeSumBST(root.left,low,high)
    ans+= rangeSumBST(root.right,low,high)

    return ans

__________________________________________________________________________________________________________________________

def rangeSumBST(root, low, high):
    if root==None:
        return 0
    
    if root.data<low:
        return rangeSumBST(root.right,low,high)
    if root.data>high:
        return rangeSumBST(root.left,low,high)

    ans=root.data
    ans+= rangeSumBST(root.left,low,high)
    ans+= rangeSumBST(root.right,low,high)

    return ans
