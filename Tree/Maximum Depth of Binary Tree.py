def max_depth(root):
    if root==None:
        return 0
    
    left_height = max_depth(root.left)
    right_height = max_depth(root.right)

    return max(left_height,right_height) + 1
