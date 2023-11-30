#Python program to print a heap as a tree-like data structure.
def print_heap_tree(heap):
    def get_tree_representation(index, level=0):
        if index < len(heap):
            left_child = 2 * index + 1
            right_child = 2 * index + 2

            
            get_tree_representation(right_child, level + 1)

           
            print('    ' * level + str(heap[index]))

           
            get_tree_representation(left_child, level + 1)

    get_tree_representation(0)


heap = [4, 10, 3, 5, 1]
print_heap_tree(heap)
