def deleteElement(head, k):
    first = second = head

    for _ in range(k):
        second = second.next

    if second==None:
        return head.next

    while second.next!=None:
        second = second.next
        first = first.next

    first.next = first.next.next

    return head
