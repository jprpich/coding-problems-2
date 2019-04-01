# Linked List representing 2 3 4 
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None 

head = Node(2)
node_a = Node(3) 
node_b = Node(4) 

head.next = node_a 
node_a.next = node_b 

def countNodes(head):
  current = head 
  count = 1
  while current.next != None:
    current = current.next 
    count += 1 
  return count 

print(countNodes(head))