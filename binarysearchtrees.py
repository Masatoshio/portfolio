
# print tree function prints the tree in a tree-like format
def print_tree(n, indent=0):
    if n is None:
        print( " " * indent, "X")
        return
    print_tree(n.right, indent+4)
    print( " " * indent, n.value)
    print_tree(n.left, indent + 4)

# BST class to initialize a binary search tree
class BST:
    class Node:
        def __init__(self, value):
            self.left = None
            self.right = None
            self.value = value

    def __init__(self):
        self.root = None

    # insert value into BST to maintain BST status
    def insert(self, value):
        # case if tree is empty
        if self.root is None:
            self.root = self.Node(value)
            return
        # search for value in tree, but keep parent in memory
        p = self.root
        prev = None
        while p is not None:
            prev = p
            if value < p.value:
                p = p.left
            else:
                p = p.right
        # insert new node with the value into the parent
        if value < prev.value:
            prev.left = self.Node(value)
        else:
            prev.right = self.Node(value)

    # prints the tree neatly for the user
    def printTree(self):
        print("-------- Tree --------")

        if self.root is None:
            print("Empty Tree")

        else:
            print_tree(self.root)

        print("----------------------")

    # removes a value from the BST and maintains BST status
    def remove(self, val):

        prev, curr = None, self.root

        while curr and curr.value != val:
            prev = curr
            if val < curr.value:
                curr = curr.left
            else:
                curr = curr.right

        if curr is None:
            return self.root

        if curr.right is None:
            if curr is self.root:
                return self.root.left

            if prev.left is curr:
                prev.left = curr.left

            else:
                prev.right = curr.left

            curr.left = None
            return self.root

        prev_succ, succ = curr, curr.right

        while succ.left:
            prev_succ = succ
            succ = succ.left

        curr.value = succ.value

        if prev_succ is curr:
            prev_succ.right = succ.right

        else:
            prev_succ.left = succ.right

        succ.right = None

        return self.root
