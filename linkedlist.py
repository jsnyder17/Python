import random

# ----------------------------------------------------------------

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

# ----------------------------------------------------------------

class LinkedStack:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, data):
        node = Node(data, None)

        if (self.head == None):
            self.head = node
        else:
            node.next = self.head
            self.head = node

        self.length += 1

    def pop(self):
        if (self.head != None):
            newHead = self.head.next
            returnNode = self.head
            self.head = None
            self.head = newHead

            self.length -= 1

            return returnNode
        else:
            print("Stack is empty. Cannot pop")

    def clear(self):
        while (self.head != None):
            self.pop()

    def populate(self, numElements):
        for x in range(numElements):
            self.append(random.randint(1, 9))

    def print(self):
        currNode = self.head

        print("{ ", end="")
        while (currNode != None):
            print(currNode.data, end=" ")
            currNode = currNode.next
        print("} (", self.length, ")", sep="")

# ----------------------------------------------------------------

stack = LinkedStack()
stack.populate(random.randint(1, 20))
stack.print()

for x in range(stack.length):
    print("Popped", str(stack.pop()), "from stack.")
    stack.print()