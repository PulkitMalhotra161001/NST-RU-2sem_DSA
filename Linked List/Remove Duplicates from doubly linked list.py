def deleteDuplicates(head):
    cur = head

    while cur!=None and cur.next!=None:

        if cur.val == cur.next.val:
            cur.next = cur.next.next
            if cur.next:
                cur.next.prev = cur
        
        else:
            cur = cur.next

    return head
