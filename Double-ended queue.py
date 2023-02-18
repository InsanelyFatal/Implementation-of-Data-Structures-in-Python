class Node:
  def __init__(self, key):
    self.key = key
    self.next = None
    self.prev = None

class MyDeque:
  def __init__(self):
    self.front = None
    self.rear= None
    self.size = 0
  
  def insertRear(self, x):
    new_node = Node(x)
    if self.front is None:
      self.front = new_node   
    else:
      self.rear.next = new_node
      new_node.prev = self.rear
    self.rear = new_node
    self.size += 1

  def insertFront(self, x):
    new_node = Node(x)
    if self.front is None:
      self.front = new_node
      self.rear = new_node
    else:
      new_node = Node(x)
      new_node.next = self.front
      self.front.prev = new_node
      self.front = new_node
    self.size += 1

  def deleteRear(self):
    if self.front is None:
      return None
    

  def deleteFront(self):
    pass

  def getFront(self):
    pass

  def getRear(self, x):
    pass

  def isEmpty(self):
    pass

  def sizeOfDeque(self):
    return self.size

  def printDeque(self):
    curr = self.front
    while curr is not None:
      print(curr.key)
      curr = curr.next
      

md = MyDeque()
md.insertFront(10)
md.insertFront(20)
md.insertFront(30)
md.insertFront(40)
md.printDeque()
print(md.sizeOfDeque())



