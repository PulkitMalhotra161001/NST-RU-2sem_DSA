def node_sum(root):
    if root==None:
        return 0
    return root.val + node_sum(root.left) + node_sum(root.right)
