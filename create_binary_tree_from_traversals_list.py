class Node:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'Node({!r})'.format(self.data)

# create tree from given pre_order and in_order traversal of tree
def create_tree(pre_order, in_order):

    """
    Function that recreates binary search tree based on a given pre order and
    in order traversal of the tree

    Recursively splits the given input into root, left and right subtrees
    """

    # print("in order", in_order)
    # print("pre order", pre_order)

    # create leaf node
    if(len(pre_order) == 0):
        return None

    if(len(pre_order) < 2):

        return Node(pre_order[0])

    root_data = pre_order[0]
    i = 0
    #print(root_data,in_order[i])
    while i < len(in_order) and in_order[i] != root_data:
        i += 1
    #     print(root_data,in_order[i])
    #
    # print("left side in order", in_order[0:i])
    # print("left side pre order", pre_order[1:i+1])
    # print("right side in order", in_order[i+1:])
    # print("right side pre order", pre_order[i+1:])
    left_sub = create_tree(pre_order[1:i+1], in_order[0:i])
    right_sub = create_tree(pre_order[i+1:], in_order[i+1:])

    root = Node(root_data)
    root.left = left_sub
    root.right = right_sub

    return root

in_order = ["d","b","e","a","f","c","g"]
pre = ["a","b","d","e","c","f","g"]

tree_root = create_tree(pre,in_order)

print(tree_root)
print(tree_root.left, tree_root.right)
print(tree_root.left.left,tree_root.left.right,tree_root.right.left,tree_root.right.right)
