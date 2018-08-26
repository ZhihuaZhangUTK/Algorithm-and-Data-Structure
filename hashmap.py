### Hash MAP ###

class hashmap:
  def __init__(self):
    self.size = 11
    self.data = [[] for _ in range(self.size)]
  
  def _get_hashing(self, key):
    idx = 0
    for s in str(key):
      idx += ord(s)
    return idx % self.size
  
  def add(self, key, value):
    idx = self._get_hashing(key)
    key_exists = False
    bucket = self.data[idx]
    for i, kv in enumerate(bucket):
      k, v = kv[0], kv[1]
      if key==k:
        key_exists = True
        break
    if key_exists:
      bucket[i] = ((key, value))
    else:
      bucket.append((key, value))
      
  def get(self, key):
    idx = self._get_hashing(key)
    bucket = self.data[idx]
    for i, kv in enumerate(bucket):
      k, v = kv
      if k==key:
        return v
    raise KeyError
  
  def print_map(self):
    print(self.data)


  def delete(self, key):
    idx = self._get_hashing(key)
    bucket = self.data[idx]
    for i, kv in enumerate(bucket):
      k, v = kv
      if k==key:
        bucket.remove((k,v))
        return
    raise KeyError  
    
hashmap = hashmap()
hashmap.add('zhihua', '867-456-3433')
hashmap.add('james', '863-567-3456')
hashmap.add('queen', '865-456-3564')
hashmap.add('chloe', '866-455-3353')
hashmap.add('jay', '865-446-3439')
hashmap.add('jaime', '865-478-3439')

print('---PHONE BOOK---')
hashmap.print_map()

print(hashmap.get('james'))
print(hashmap.get('jay'))

hashmap.delete('jay')
hashmap.print_map()

hashmap.delete('jaly')
