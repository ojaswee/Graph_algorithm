#linked list

class Node:
    def __init__(self, _id):
        self.id = _id
        self.Next = None
        self.previous = None

class LL:
    def __init__(self):
        self.head = None
        self.countNodes = 0

    def addNode(self, id):
        newNode = Node(id)  # first make the received value a node
        currentNode = self.head

        if self.head is None:
            self.head = newNode
            self.countNodes +=1
        else:
            # if there is head already
            currentNode.next = newNode
            self.countNodes += 1
        print newNode.id,'\t', self.countNodes

newLL = LL()

newLL.addNode(5)
newLL.addNode(10)
newLL.addNode(3)
