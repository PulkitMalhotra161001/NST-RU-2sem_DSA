'''
class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
'''
ans = []
def postorder_traversal(root):
    if root==None:
        return []

    # left
    postorder_traversal(root.left)
    # right
    postorder_traversal(root.right)
    # node
    ans.append(root.val)

    return ans
