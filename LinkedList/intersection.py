from LinkedList import LinkedList

def intersection(ll1, ll2):
    """
    check if two linked list are intersected
    :param ll1:
    :param ll2:
    :return: boolean
    """
    curr1 = ll1.head
    curr2 = ll2.head
    if len(ll1) > len(ll2):
        for _ in range(len(ll1) - len(ll2)):
            curr1 = curr1.next
    else:
        for _ in range(len(ll2) - len(ll1)):
            curr2 = curr2.next
    while curr1 and curr2:
        if curr1 is curr2:
            return True
        curr1 = curr1.next
        curr2 = curr2.next
    return False
