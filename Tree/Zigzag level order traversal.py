from queue import Queue

def zigzag_level_order(root):
    q = Queue()
    q.put(root)
    level = 1
    ans = []
    while q.qsize()>0:

        sz = q.qsize()
        temp = []
        for _ in range(sz):
            node = q.get()
            temp.append(node.val)

            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        if level%2==0:
            temp.reverse()
        level+=1
        ans.append(temp)
    
    return ans
