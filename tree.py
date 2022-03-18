class Node(object):
    def __init__(self, data, right_node, left_node):
        self.right_node = right_node
        self.left_node = left_node
        self.data = data

    def print_node(self):
        print(self.data)

def print_browse(node):
    print(node.data)
    if node.right_node==None and node.left_node==None:
        print('Leaf atteined')
    if node.right_node!=None:
        print_browse(node.right_node)
    if node.left_node!=None:
        print_browse(node.left_node)


def tree_generator(node, depth, nb):
    if depth != 0:
        node.right_node = Node(nb, left_node=None, right_node=None)
        tree_generator(node.right_node, depth - 1, nb + 1)
        nb += 1
        node.left_node = Node(nb, left_node=None, right_node=None)
        tree_generator(node.left_node, depth - 1, nb + 1)
        nb += 1
    if depth == 0:
        nb += 1


def tree_population(depth, nb):
    root_node = Node(0, left_node=None, right_node=None)
    tree_generator(root_node, depth, nb)
    return root_node

depth, nb = 3, 1
root_node = tree_population(depth, nb)

print_browse(root_node)