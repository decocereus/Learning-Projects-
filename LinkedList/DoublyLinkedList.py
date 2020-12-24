class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def printList(self):
        if self.head is None:
            print("Empty List")
        else:
            temp = self.head 
            while(temp.next):
                print(temp.data)
                temp = temp.next 
                
    def insertInEmptyList(self, data):
        if self.head is None:
            nodeToAdd = Node(data)
            self.head = nodeToAdd
        else:
            print("List is not empty.")
            
    def insterAtHead(self,data):
        if self.head is None:
            nodeToAdd = Node(data)
            self.head = nodeToAdd
        else:
            nodeToAdd = Node(data)
            nodeToAdd.next = self.head 
            self.head.prev = nodeToAdd
            self.head = nodeToAdd
            


dLL = DoublyLinkedList()
dLL.insertInEmptyList(0)
dLL.insterAtHead(2)
dLL.insterAtHead(1)
dLL.insertInEmptyList(0)


print("This is our list: \n")
dLL.printList()
