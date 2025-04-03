def merge(head1,head2):
    if head1==None:
        return head2
    
    if head2==None:
        return head1

    cur = head1
    while cur.next!=None:
        cur = cur.next
    
    cur.next = head2
    return head1
