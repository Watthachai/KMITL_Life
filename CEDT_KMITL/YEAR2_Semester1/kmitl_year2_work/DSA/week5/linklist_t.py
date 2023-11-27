class PriNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.headsec = None


class LinkList:
    def __init__(self):
        self.head = None

    def pushPri(self, node):
        if self.head == None:
            self.head = node
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = node

    def printNode(self):
        temp = []
        p = self.head
        while p:
            print(p.data)
            p = p.next


linklistt = LinkList()
node = PriNode("A")
linklistt.pushPri(node)
linklistt.printNode()
