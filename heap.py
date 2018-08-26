####  Max Heap  ####

class heap:
  def __init__(self):
    self.heap_list = [0]
    self.current_size = 0

  def insert(self, value):
    self.heap_list.append(value)
    self.current_size += 1
    self._goup(self.current_size)

  def _goup(self, size):
    parent = size // 2
    if parent>0 and self.heap_list[parent] < self.heap_list[size]:
      self._swap(self.heap_list, parent, size)
    if parent <=0:
      return
    else:
      self._goup(parent)

  def _swap(self,A, i, j):
    A[i], A[j] = A[j], A[i]
    return

  def heap_print(self):
    print(self.heap_list[1:])

  def percDown(self,i):
    while (i * 2) <= self.current_size:
      mc = self.maxChild(i)
      if self.heap_list[i] < self.heap_list[mc]:
        self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
      i = mc

  def maxChild(self,i):
    if i * 2 + 1 > self.current_size:
      return i * 2
    else:
      if self.heap_list[i*2] > self.heap_list[i*2+1]:
        return i * 2
      else:
        return i * 2 + 1
      
  def delMax(self):
    retval = self.heap_list[1]
    self.heap_list[1] = self.heap_list[self.current_size]
    self.current_size = self.current_size - 1
    self.heap_list.pop()
    self.percDown(1)
    return retval


heap = heap()
heap.insert(2)
heap.insert(4)
heap.insert(7)
heap.heap_print()
heap.insert(3)
heap.insert(8)
heap.insert(5)
heap.heap_print()

print(heap.delMax())
heap.heap_print()
