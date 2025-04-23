def invert_binary_tree(root):
    if root==None:
        return root

    root.left, root.right = root.right, root.left
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return root
