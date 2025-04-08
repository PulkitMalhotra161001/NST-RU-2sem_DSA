def splitList(head, head1, head2):
    
    slow = head
    fast = head
    while fast.next.next!=head and fast.next!=head:
        fast = fast.next.next
        slow = slow.next

    # we have even no. of nodes
    if fast.next.next == head:
        # then fast will point to last node
        fast = fast.next

    head1 = head
    head2 = slow.next

    slow.next = head1
    fast.next = head2

    return head1, head2
