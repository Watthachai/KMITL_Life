from collections import deque
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
                    
            else: 
                self.data = data
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()    
                
    def inOrderTraversal(self, root):
        res = []
        if root:
            res = self.inOrderTraversal(root.left)
            res.append(root.data)
            res = res + self.inOrderTraversal(root.right)
        return res

    def preOrderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preOrderTraversal(root.left)
            res = res + self.preOrderTraversal(root.right)
        return res

    def postOrderTraversal(self, root):
        res = []
        if root:
            res = self.postOrderTraversal(root.left)
            res = res + self.postOrderTraversal(root.right)
            res.append(root.data)
        return res

        
    def breathFirstTraversal(self, root):
        res = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            res.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return res
            
root = Node(15)

root.insert(15)
root.insert(3)
root.insert(16)
root.insert(9)
root.insert(23)
root.insert(11)
root.insert(7)
root.insert(5)
root.insert(34)
root.insert(19)
root.insert(2)

root.PrintTree()

print(f"Inorder traversal: {root.inOrderTraversal(root)}")
print(f"Preorder traversal: {root.preOrderTraversal(root)}")
print(f"Postorder traversal: {root.postOrderTraversal(root)}")
print(f"Level-order traversal: {root.breathFirstTraversal(root)}")