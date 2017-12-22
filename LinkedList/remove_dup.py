import unittest
from LinkedList import LinkedList

def remove_dup_my_solution(ll):
    """
    remove duplicate from an unsorted linked list
    :param ll:
    :return:
    """
    if not ll.head:
        return None
    hashset = set()
    head = ll.head
    hashset.add(head.value)
    prev = head
    curr = head.next
    while curr:
        if curr.value not in hashset:
            hashset.add(curr.value)
        else:
            while curr and curr.value in hashset:
                curr = curr.next
            if curr:
                hashset.add(curr.value)
            prev.next = curr
        prev = curr
        if curr:
            curr = curr.next
    return head


def remove_dup_better(ll):
    """
    better solution
    :param ll:
    :return:
    """
    if not ll.head:
        return None
    curr = ll.head
    seen = set([curr.value])
    while curr.next:
        if curr.next.value not in seen:
            seen.add(curr.next.value)
            curr = curr.next
        else:
            curr.next = curr.next.next
    return ll

def remove_dup_without_memory(ll):
    """
    implemented it without memory
    :param ll:
    :return:
    """
    if not ll.head:
        return None
    curr = ll.head
    while curr:
        runner = curr
        while runner.next:
            if runner.next.value == curr.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curr = curr.next
    return ll

ll = LinkedList()
ll.generate(100, 0, 9)
print(ll)
remove_dup_without_memory(ll)
print(ll)