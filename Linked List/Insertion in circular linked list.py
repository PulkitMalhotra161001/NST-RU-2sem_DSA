def insertion(head, K):
    dummy = Node(K)

    cur = head
    while cur.next!=head:
        cur = cur.next

    cur.next = dummy
    dummy.next = head

    return head
