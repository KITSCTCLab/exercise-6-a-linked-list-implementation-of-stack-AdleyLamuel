class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
    struct Node* newnode = (struct Node*) malloc(sizeof(struct Node))
    newnode.data = val
    newnode.next = top
    top = newnode
    
  def pop(self) -> None:
    if(top==NULL):
        print("Stack Underflow")
    else:
        struct Node* temp = top
        print("The popped element is ", top.data)
        top = top.next
        free (temp)
  
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
