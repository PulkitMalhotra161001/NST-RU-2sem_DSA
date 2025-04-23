dictionary = {}
def parentStorer(node, parent = None):
    if node == None:
        return 

    dictionary[node] = parent 
    parentStorer(node.left, node)
    parentStorer(node.right, node)  

def lowest_common_ancestor(root, node1, node2):
    parentStorer(root)

    curr_node = node1 
    path1 = []
    while curr_node != root:
        path1.append(curr_node)
        curr_node = dictionary[curr_node]
    path1.append(root)

    curr_node = node2 
    path2 = []
    while curr_node != root:
        path2.append(curr_node)
        curr_node = dictionary[curr_node]
    path2.append(root)
    
    path1.reverse()
    path2.reverse()

    i, j = 0, 0
    ans = None 
    while i < len(path1) and j < len(path2):
        if path1[i] == path2[j]:
            ans = path1[i]
        if path1[i] != path2[j]:
            break 
        i += 1
        j += 1
    return ans


____________________________________________________________________________________________________


def  lowest_common_ancestor(root, node1, node2):
    if root == None:
        return None 

    if root == node1 or root == node2:
        return root 
    
    left = lowest_common_ancestor(root.left, node1, node2)
    right = lowest_common_ancestor(root.right, node1, node2)

    if left != None and right != None:
        return root 
    
    return left or right
