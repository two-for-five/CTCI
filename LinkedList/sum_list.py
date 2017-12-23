from LinkedList import LinkedList

def sum_list(ll1, ll2):
    curr1 = ll1.head
    curr2 = ll2.head
    res = LinkedList()
    add_one = False
    while curr1 or curr2:
        if curr1 and curr2:
            digit = curr1.value + curr2.value
            curr1 = curr1.next
            curr2 = curr2.next
        elif curr1:
            digit = curr1.value
            curr1 = curr1.next
        elif curr2:
            digit = curr2.value
            curr2 = curr2.next
        if add_one:
            digit += 1
            add_one = False
        if digit >= 10:
            add_one = True
            digit = digit % 10
        res.add(digit)
    return res

def sum_list_follow(ll1, ll2):
    """
    follow up forward order
    :param ll1:
    :param ll2:
    :return:
    """
    if len(ll1) < len(ll2):
        for _ in range(len(ll2) - len(ll1)):
            ll1.add_to_beginning(0)
    else:
        for _ in range(len(ll1) - len(ll2)):
            ll2.add_to_beginning(0)
    num = 0
    curr1 = ll1.head
    curr2 = ll2.head
    res = LinkedList()
    while curr1 and curr2:
        num = (num * 10) + curr1.value + curr2.value
        curr1 = curr1.next
        curr2 = curr2.next
    res.add_multiple([int(i) for i in str(num)])
    return res

ll_a = LinkedList()
ll_a.generate(4, 0, 9)
ll_b = LinkedList()
ll_b.generate(3, 0, 9)
print(ll_a)
print(ll_b)
print(sum_list(ll_a, ll_b))


print(sum_list_follow(ll_a, ll_b))


