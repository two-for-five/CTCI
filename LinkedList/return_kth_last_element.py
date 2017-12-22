from LinkedList import LinkedList

def return_kth_last_element(ll, k):

   curr = runner = ll.head
   for i in range(k):
       if not runner:
           return None
       runner = runner.next
   while runner:
       runner = runner.next
       curr = curr.next

   return curr


test = LinkedList()
test.generate(5, 0, 10)
print(test)
print(return_kth_last_element(test, 2))
