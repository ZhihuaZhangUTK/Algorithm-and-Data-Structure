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
      elems.append(cur_node.data)
    print(elems)
    
  def get(self,index):
    if index >= self.length():
      print('ERROR: get index out of range')
    cur_idx = 0
    cur_node = self.head
    while True:
      cur_node = cur_node.next
      if cur_idx == index: return cur_node.data
      cur_idx += 1


  def erase(self,index):
    if index >= self.length():
      print('ERROR: get index out of range')
      return 
    cur_idx = 0
    cur_node = self.head
    while True:
      last_node = cur_node
      cur_node = cur_node.next
      if cur_idx == index:
        if cur_node.next:
          last_node.next = cur_node.next
        else:
          last_node.next = None
        break
      cur_idx += 1
      
  def insert(self, index, data):
    if index >= self.length():
      print('ERROR: insert index out of range')
      return
    if index <0:
        print('ERROR: index cannot be negative')
    cur_idx = 0
    cur_node = self.head
    while True:
        last_node = cur_node
        cur_node = cur_node.next
        if cur_idx == index:
          new_node = node(data)
          last_node.next = new_node
          new_node.next = cur_node
          return
        cur_idx += 1

  def set(self,index,data):
    if index>=self.length() or index<0:
      print("ERROR: 'Set' Index out of range!")
      return
    cur_node=self.head
    cur_idx=0
    while True:
      cur_node=cur_node.next
      if cur_idx==index:
          cur_node.data=data
          return
      cur_idx+=1


my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()

print("element at 2nd index: %d" % my_list.get(0))
my_list.erase(3)
my_list.display()
my_list.erase(0)
my_list.display()
my_list.insert(0,5)
my_list.insert(2,4)
my_list.display()


my_list.set(3,40)
my_list.display()
