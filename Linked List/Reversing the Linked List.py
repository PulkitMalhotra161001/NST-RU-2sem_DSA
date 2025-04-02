def reverseLL(head):
    prev = None 
    temp = head.next 

    while temp != None:
        head.next = prev 
        prev = head 
        head = temp 
        temp = temp.next 
    head.next = prev 
    return head
