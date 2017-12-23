from LinkedList import LinkedList

def loop_detection(ll):
    curr = ll.head
    hashset = set()
    while curr:
        if curr.value not in hashset:
            hashset.add(curr.value)
        else:
            return curr.value
    return False


def loop_detection_without_memory(ll):
    fast = ll.head
    slow = ll.head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break
    if not fast or not fast.next:
        return None
    slow = ll.head
    while fast is not slow:
        fast = fast.next
        slow = slow.next
    return fast