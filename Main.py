class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
    if self.head is None:
        self.head = Node(data)
    else:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
  def pop(self) -> None:
    if self.head is None:
        return None
    else:
        popped = self.head.data
        self.head = self.head.next
        return popped
  
  def status(self):
    struct Node* ptr
    if(top==NULL):
        cout<<"stack is empty";
    else: 
        ptr = top
    print("Stack elements are: ")
    while (ptr != NULL):
      print(ptr.data, " ")
      ptr = ptr->next

# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
