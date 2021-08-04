class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.Height = 0

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        else:
            node = self.root
            Height = 0
            while True:
                Height += 1
                if data < node.data :
                    if node.left is None:
                        node.left = Node(data)
                        if self.Height < Height:
                            self.Height = Height
                        return
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = Node(data)
                        if self.Height < Height:
                            self.Height = Height
                        return
                    else:
                        node = node.right
            

if __name__ == '__main__':
    T = BST()
    inp = [int(i) for i in input('Enter Input : ').split()]
    for i in inp:
        root = T.insert(i)
    print("Height of this tree is :",T.Height)