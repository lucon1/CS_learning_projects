# Problem Set 4A
# Name:
# Collaborators:

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8,Node(2,Node(1),Node(6)),Node(10))
tree2 = Node(7,Node(2,Node(1),Node(5,Node(3),Node(6))),Node(9,Node(8),Node(10)))
tree3 = Node(5,Node(3,Node(2),Node(4)),Node(14,Node(12),Node(21,Node(20),Node(26))))

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    # TODO: Remove pass and write your code here
    height = 0
    #check if there are children
    if tree == None:
        return height
    if Node.get_left_child(tree) != None or Node.get_right_child(tree) != None:
        height += 1 + max(find_tree_height(Node.get_left_child(tree)),find_tree_height(Node.get_right_child(tree)))
        return height
    else:
        return height
    
print(find_tree_height(tree2))

def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    # TODO: Remove pass and write your code here
    if tree == None:
        return True
    
    left = Node.get_left_child(tree)
    left_is_heap = True
    right = Node.get_right_child(tree)
    right_is_heap = True
    tree_value = tree.get_value()

    if left == None and right == None:
        return True
    
    if left != None:
        left_value = left.get_value()
        left_is_heap = is_heap(left, compare_func)
        if left_is_heap:
            left_is_heap = compare_func(left_value,tree_value)
    if right != None:
        right_value = right.get_value()
        right_is_heap = is_heap(right, compare_func)
        if right_is_heap:
            right_is_heap = compare_func(right_value,tree_value)
        
    if left_is_heap and right_is_heap:
        return True


    # if tree == None:
    #     return True
    
    # left = Node.get_left_child(tree)
    # right = Node.get_right_child(tree)
    # tree_value = tree.get_value()

    # if left == None and right == None:
    #     return True
    
    # if left != None:
    #     left_value = left.get_value()
    #     left_is_heap = is_heap(left, compare_func)
    # if right != None:
    #     right_value = right.get_value()
    #     right_is_heap = is_heap(right, compare_func)
        
    # if left_is_heap and right_is_heap:
    #     return compare_func(left_value,tree_value) and compare_func(right_value,tree_value)


if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass
