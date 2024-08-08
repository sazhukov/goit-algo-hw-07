import matplotlib.pyplot as plt
import networkx as nx

class BinaryTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.parent = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return BinaryTreeNode(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def delete_node(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)

    return root

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def search(root, key):
    if root is None or root.key == key:
        return root
    if root.key < key:
        return search(root.right, key)
    return search(root.left, key)

def find_max_value(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.key

def find_min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.key

def sum_of_values(node):
    if node is None:
        return 0
    return node.key + sum_of_values(node.left) + sum_of_values(node.right)

def visualize_binary_tree(root):
    G = nx.DiGraph()

    def add_edges(node):
        if node is not None:
            G.add_node(node.key)
            if node.left:
                G.add_edge(node.key, node.left.key)
                add_edges(node.left)
            if node.right:
                G.add_edge(node.key, node.right.key)
                add_edges(node.right)

    add_edges(root)
    pos = nx.spring_layout(G)  # Compute node positions

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, arrows=False, node_size=2000, node_color='lightblue', font_size=12, font_weight='bold')
    plt.title("Binary Tree Visualization")
    plt.show()

if __name__ == '__main__':
    root = None
    keys = [5, 3, 8, 2, 4, 7, 9]

    for key in keys:
        root = insert(root, key)
        print("Inserted:", key)
        print("Binary Tree:")
        print(root)

    # Delete
    keys_to_delete = [8, 3]
    for key in keys_to_delete:
        root = delete_node(root, key)
        print("Deleted:", key)
        print("Binary Tree:")
        print(root)

    # Assume root is the root of your binary tree
    search_key = 7
    result = search(root, search_key)
    if result:
        print(f"Value {search_key} found in Binary Tree.")
    else:
        print(f"Value {search_key} not found in Binary Tree.")

    max_value = find_max_value(root)
    min_value = find_min_value(root)
    total_sum = sum_of_values(root)

    print("Maximum value:", max_value)
    print("Minimum value:", min_value)
    print("Sum of all values:", total_sum)

    visualize_binary_tree(root)
