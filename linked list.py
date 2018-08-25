##Linked list###
#Single Linked List / Double Linked List

class node:
  def __init__(self, data=None):
    self.data = data
    self.next = None
    
class linked_list:
  def __init__(self):
    self.head = node()
    
  def append(self, data):
    new_node = node(data)
    cur = self.head
    while cur.next:
      cur = cur.next
    cur.next = new_node
   
  def length(self):
    cur = self.head
    total = 0
    while cur.next:
      total+=1
      cur = cur.next
    return total
 
  def display(self):
    elems = []
    cur_node = self.head
    while cur_node.next:
      cur_node = cur_node.next
      elems.append(cur_node,data)
    print(elems)

my_list = linked_list()
my_list.display()
