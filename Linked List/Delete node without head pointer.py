def deleteNode(curr_node):
    curr_node.data = curr_node.next.data
    curr_node.next = curr_node.next.next
