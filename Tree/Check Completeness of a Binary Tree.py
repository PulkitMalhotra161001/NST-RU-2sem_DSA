from queue import Queue
def is_complete_tree(root):
    q = Queue()
    q.put(root)
    found_None = False

    while q.qsize()>0:

        node = q.get()
        
        if node==None:
            found_None = True
        else:
            # we have found 'None' node before and current node is 'Not_Null'
            if found_None:
                return False
            q.put(node.left)
            q.put(node.right)
        
    return True
