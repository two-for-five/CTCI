from LinkedList import LinkedList

def partition(ll, k):
    """
    partition based on K
    :param ll:
    :param k:
    :return:
    """
    if not ll.head:
        return None
    before = LinkedList()
    after = LinkedList()
    curr = ll.head
    while curr:
        if curr.value < k:
            before.add(curr.value)
        else:
            after.add(curr.value)
        curr = curr.next
    temp = before.head
    while temp.next:
        temp = temp.next
    temp.next = after.head
    return before

ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
new_ll = partition(ll, ll.head.value)
print(new_ll)


