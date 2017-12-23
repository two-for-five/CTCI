from LinkedList import LinkedList

def is_palindrome(ll):
    """
    check if the ll is a palindrome
    :param ll:
    :return: boolean
    """
    fast = ll.head
    slow = ll.head
    stack = []
    while fast and fast.next:
        fast = fast.next.next
        stack.insert(0, slow.value)
        slow = slow.next
    if fast:
        slow = slow.next
    while slow:
        char = stack.pop(0)
        if char != slow.value:
            return False
        slow = slow.next
    return True

ll_true = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(is_palindrome(ll_true))
ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(is_palindrome(ll_false))