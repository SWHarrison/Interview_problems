# new methods added on lines 63 and

#!python
#from queue import Queue
#from stack import Stack
#from linkedlist import LinkedList

class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # TODO: Check if both left child and right child have no value
        return self.left == None and self.right == None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # TODO: Check if either left child or right child has a value
        return (self.left != None or self.right != None)

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Best case: O(1) when node is a leaf
        Worst case: O(n) when node is root and n is items in tree"""
        if(self.is_leaf()):  # base case
            return 0
        left = 0
        right = 0
        if(self.left):
            left = self.left.height()  # traverse left subtree
        if(self.right):
            right = self.right.height()  # traverse right subtree
        # alternate way using ternary expression:
        #right = self.right.height() if self.right else 0

        return 1 + max(left,right)  # visit current node


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def two_sum(self, target):

        nums = self.items_in_order()

        hash_list = {}
        to_return = []

        for num in nums:
            pair = target - num
            if num in hash_list:
                to_return.append((num,pair))
            else:
                hash_list[pair] = 1

        return to_return

    def superbalanced(self):

        current_node = self.root

        if current_node == None:
            return True

        heights = []

        self._superbalanced_helper(self.root, heights.append, 0)

        print("all heights",heights)

        if max(heights) - min(heights) <= 1:
            return True
        else:
            return False

    def _superbalanced_helper(self, node, visit, height):

        print("node is",node)
        if(node is not None):
            print(node.is_leaf())
            self._superbalanced_helper(node.left, visit, height + 1)
            if node.is_leaf():
                print("adding height",height)
                visit(height)
            self._superbalanced_helper(node.right, visit, height + 1)



    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        Best case: O(1) when root is a leaf
        Worst case: O(n) when node is root and n is items in tree"""
        if(not self.is_empty()):
            return self.root.height()

        return None

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        Best case: O(1) when root has the item
        Worst case: O(log n) when node is lowest level of tree"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        Best case: O(1) when root has the item
        Worst case: O(log n) when node is lowest level of tree"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # TODO: Return the node's data if found, or None
        return node.data if node else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        Best case: O(1) when adding to empty tree
        Worst case: O(log n) when node is lowest level of tree"""
        # Handle the case where the tree is empty
        if self.is_empty():
            self.root = BinaryTreeNode(item)
            self.size += 1
            return
        parent = self._find_parent_node_recursive(item, self.root)
        if item < parent.data:
            parent.left = BinaryTreeNode(item)
            self.size += 1
        elif item > parent.data:
            parent.right = BinaryTreeNode(item)
            self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        Best case: O(1) when root has the item
        Worst case: O(log n) when node is lowest level of tree"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            if node.data == item:
                return node
            elif node.data > item:
                node = node.left
            elif node.data < item:
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        Best case: O(1) when root has the item
        Worst case: O(log n) when node is lowest level of tree"""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        elif node.data == item:
            # Return the found node
            return node
        elif item < node.data:
            return self._find_node_recursive(item, node.left)
        elif item > node.data:
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        Best case: O(1) when root has the item
        Worst case: O(log n) when node is lowest level of tree"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            if node.data == item:
                # Return the parent of the found node
                return parent
            elif item < node.data:
                parent = node
                node = node.left
            elif item > node.data:
                parent = node
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion).
        Best case: O(1) when root has the item
        Worst case: O(log n) when node is lowest level of tree"""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return parent
        if node.data == item:
            # Return the parent of the found node
            return parent

        elif item < node.data:
            parent = node
            return self._find_parent_node_recursive(item, node.left, parent)
        elif item > node.data:
            parent = node
            return self._find_parent_node_recursive(item, node.right, parent)

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        Best case: O(1) when root has the item and tree is otherwise empty
        Worst case: O(log n) when predecessor/successor is in lowet level of tree"""

        #parent = self._find_parent_node_iterative(item)
        parent = self._find_parent_node_recursive(item, self.root)
        node = None
        if(parent == None):
            #node = self._find_node_iterative(item)
            node = self._find_node_recursive(item, self.root)
        elif(item < parent.data):
            node = parent.left
        else:
            node = parent.right
        print("Node is",node)
        if(node == None):
            raise ValueError("Item not in tree!")

        if(node.is_leaf()):
            print(node, "is leaf")
            if(node == self.root):
                self.root = None
                return

            if(node.data < parent.data):
                parent.left = None
            else:
                parent.right = None

        elif(node.is_branch()):
            print(node, "is branch")

            if(node.left and node.right):
                #find predecessor
                if(node.left != None):
                    current = node.left
                    parent = node
                    while(current.right and not current.is_leaf()):
                        parent = current
                        current = current.right

                    node.data = current.data
                    if(parent != node):
                        parent.right = None
                    else:
                        parent.left = None

                #find successor, unused after changes to delete
                '''else:
                    current = node.right
                    parent = node
                    while(current.left and not current.is_leaf()):
                        parent = current
                        current = current.left

                    node.data = current.data
                    if(parent != node):
                        parent.left = None
                    else:
                        parent.right = None'''
            else:
                #only left child exists
                if(node.left):
                    next_node = node.left
                    new_data = next_node.data
                    node.data = new_data
                    node.left = next_node.left
                    node.right = next_node.right
                    next_node.right = None
                    next_node.left = None
                #only right child exists
                elif(node.right):
                    next_node = node.right
                    new_data = next_node.data
                    node.data = new_data
                    node.left = next_node.left
                    node.right = next_node.right
                    next_node.right = None
                    next_node.left = None

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) as it must visit each node
        Memory usage: Stores up to log n items, as it must fully traverse
        each subtree, with the longest path being log n."""
        if(node is not None):
            self._traverse_in_order_recursive(node.left, visit)
            visit(node.data)
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) as it must visit each node
        Memory usage: Stores up to log n items, as it must fully traverse
        each subtree, with the longest path being log n."""
        stack = Stack()
        stack.push(node)
        while not stack.is_empty():
            if(stack.peek().left != None):
                stack.push(stack.peek().left)
            else:
                node = stack.pop()  # child of next node to be popped
                visit(node.data)
                if(not stack.is_empty() and node.right == None):
                    node = stack.pop()  # parent of node previously popped
                    visit(node.data)
                if(node.right is not None):
                    stack.push(node.right)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_iterative(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) as it must visit each node
        Memory usage: Stores up to log n items, as it must fully traverse
        each subtree, with the longest path being log n."""
        if(node is not None):
            visit(node.data)
            self._traverse_pre_order_recursive(node.left, visit)
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) as it must visit each node
        Memory usage: Stores up to log n items, as it must fully traverse
        each subtree, with the longest path being log n."""
        stack = Stack()
        stack.push(node)
        while not stack.is_empty():
            node = stack.pop()
            visit(node.data)
            if(node.right != None):
                stack.push(node.right)
            if(node.left != None):
                stack.push(node.left)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []  # original
        def array_prepend(item):  # closure on items variable
            items.insert(0, item)  # O(n) -- too slow

        llist = LinkedList()  # linked version
        def llist_prepend(item):  # closure on llist variable
            llist.prepend(item)  # O(1) -- fast

        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            #self._traverse_post_order_recursive(self.root, items.append)  # original
            #self._traverse_post_order_iterative(self.root, array_prepend)  # hacked version
            self._traverse_post_order_iterative(self.root, llist_prepend)  # linked version
            # items = self._traverse_post_order_iterative(self.root)
        # Return post-order list of all items in tree
        # return items  # original
        return llist.items()  # linked version  # O(n)

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) as it must visit each node
        Memory usage: Stores up to log n items, as it must fully traverse
        each subtree, with the longest path being log n."""
        if(node is not None):
            self._traverse_post_order_recursive(node.left, visit)
            self._traverse_post_order_recursive(node.right, visit)
            visit(node.data)

    def _traverse_post_order_iterative(self, node, visit = None):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) as it must visit each node
        Memory usage: Stores up to log n items, as it must fully traverse
        each subtree, with the longest path being log n."""
        # Unused code using set to ensure no duplicates
        '''stack = Stack()
        stack.push(node)
        visited = set()
        while not stack.is_empty():
            if(stack.peek().left != None and stack.peek().left.data not in visited):
                stack.push(stack.peek().left)
            elif(stack.peek().right != None and stack.peek().right.data not in visited):
                stack.push(stack.peek().right)
            else:
                node = stack.pop()
                visit(node.data)
                visited.add(node.data)'''

        #items = [None] * self.size

        #i = self.size
        stack = Stack()
        stack.push(node)
        while not stack.is_empty():
            #i -= 1
            node = stack.pop()
            #items[i] = node.data
            visit(node.data)
            if(node.left != None):
                stack.push(node.left)
            if(node.right != None):
                stack.push(node.right)

        #return items



    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n) as it must visit each node
        Memory usage: Stores up to 2 to the power of heigh of tree,
        as it must fully traverse node and store it's children, meaning
        the queue at one point stores every node in the bottom level, which
        has a max number of nodes of 2^h """
        queue = Queue()
        queue.enqueue(start_node)
        while not queue.is_empty():
            node = queue.dequeue()
            visit(node.data)
            if(node.left != None):
                queue.enqueue(node.left)
            if(node.right != None):
                queue.enqueue(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    #items = [2, 1, 3]
    #items = [4, 2, 6, 1, 3, 5, 7]
    items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print(tree.root.height())

    '''print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))'''

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))

    print("Testing deletion ******")
    tree.delete(4)
    print('items in-order:    {}'.format(tree.items_in_order()))
    print("root is",tree.root)
    print("root right is",tree.root.right)
    print("root left is",tree.root.left)
    tree.delete(6)
    print('items in-order:    {}'.format(tree.items_in_order()))
    tree.delete(5)
    print('items in-order:    {}'.format(tree.items_in_order()))


if __name__ == '__main__':
    #test_binary_search_tree()
    #items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    items = [1,2,3,4,5,0]
    tree = BinarySearchTree(items)
    print(tree.superbalanced())
