import random

from Doubly_Linked_Lists import DoublyLinkedList
from Queues import Queue
from Stacks import Stack
from Hash_Maps import HashMap
from Binary_Search_Tree import BinarySearchTree
from Max_Heaps import MaxHeap
from Graphs import Graph, Vertex


def test_doubly_linked_list():
    print("Testing Doubly Linked List...")

    print("Creating a subway line...")
    subway = DoublyLinkedList()

    subway.add_to_head("Times Square")
    subway.add_to_head("Grand Central")
    subway.add_to_head("Central Park")

    print(subway.stringify_list())
    print("Adding new stops to our line...")

    subway.add_to_tail("Penn Station")
    subway.add_to_tail("Wall Street")
    subway.add_to_tail("Brooklyn Bridge")

    print(subway.stringify_list())
    print("Removing the first and last stop from our line...")

    subway.remove_head()
    subway.remove_tail()

    print(subway.stringify_list())

    print("Times Square station is under construction, temporarily removing it from the line...")
    subway.remove_by_value("Times Square")

    print(subway.stringify_list())


def test_stack():
    print("Defining an empty pizza stack with a max depth of 6 pizzas...")
    pizza_stack = Stack(6)

    # Adding pizzas as they are ready until we have
    pizza_stack.push("pizza #1")
    pizza_stack.push("pizza #2")
    pizza_stack.push("pizza #3")
    pizza_stack.push("pizza #4")
    pizza_stack.push("pizza #5")
    pizza_stack.push("pizza #6")

    pizza_stack.push("pizza #7")

    print("Delivering pizzas from the top of the stack down...")
    print("The first pizza to deliver is " + pizza_stack.peek())
    pizza_stack.pop()
    pizza_stack.pop()
    pizza_stack.pop()
    pizza_stack.pop()
    pizza_stack.pop()
    pizza_stack.pop()
    pizza_stack.pop()


def test_queue():
    print("Creating a deli line with up to 10 orders...\n------------")
    deli_line = Queue(10)

    print("Adding orders to our deli line...\n------------")
    deli_line.enqueue("egg and cheese on a roll")
    deli_line.enqueue("bacon, egg, and cheese on a roll")
    deli_line.enqueue("toasted sesame bagel with butter and jelly")
    deli_line.enqueue("toasted roll with butter")
    deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
    deli_line.enqueue("two fried eggs with home fries and ketchup")
    deli_line.enqueue("egg and cheese on a roll with jalapenos")
    deli_line.enqueue("plain bagel with plain cream cheese")
    deli_line.enqueue("blueberry muffin toasted with butter")
    deli_line.enqueue("bacon, egg, and cheese on a roll")
    # ------------------------ #

    deli_line.enqueue("western omelet with home fries")
    # ------------------------ #
    print("------------\nOur first order will be " + deli_line.peek())
    print("------------\nNow serving...\n------------")
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    deli_line.dequeue()
    # ------------------------ #

    deli_line.dequeue()
    # ------------------------ #


def test_hash_map():
    print("Creating geology hash array of size 15...")
    hash_map = HashMap(15)

    print("Adding our values and their respective keys to the hash map...")
    hash_map.assign('gabbro', 'igneous')
    hash_map.assign('sandstone', 'sedimentary')
    hash_map.assign('gneiss', 'metamorphic')

    print("Retrieving our values from the hash map using the keys...")
    print(hash_map.retrieve('gabbro'))
    print(hash_map.retrieve('sandstone'))
    print(hash_map.retrieve('gneiss'))


def test_binary_search_tree():
    print("Creating our tree object...")
    tree = BinarySearchTree(1)

    for x in range(20): tree.insert(random.randint(0, 200))

    print("Printing in-order depth-first traversal:")
    tree.depth_first_traversal()


def test_max_heap():
    print("Testing MaxHeap...")

    # Create a new MaxHeap instance
    max_heap = MaxHeap()

    # Test adding elements to the MaxHeap
    elements = [10, 20, 30, 40, 50, 60, 70]
    for element in elements:
        max_heap.add(element)

    # Expected max_heap.heap_list after adding elements:
    # [None, 70, 40, 60, 10, 30, 20, 50]
    expected_heap_list = [None, 70, 40, 60, 10, 30, 20, 50]

    if max_heap.heap_list == expected_heap_list:
        print("\nAdding elements to the MaxHeap: Passed")
    else:
        print("\nAdding elements to the MaxHeap: Failed")
        print("Expected:", expected_heap_list)
        print("Actual:", max_heap.heap_list)

    print()


def test_max_heap_random_input():
    print("Testing MaxHeap with random input...")

    # Create a new MaxHeap instance
    max_heap = MaxHeap()

    # Test adding random elements to the MaxHeap
    elements = [random.randint(1, 100) for _ in range(10)]

    print("Adding the following random elements to the MaxHeap:", elements)

    for element in elements:
        max_heap.add(element)

    # Check if the MaxHeap property holds for all elements
    is_max_heap = True
    for idx, element in enumerate(max_heap.heap_list[1:], start=1):
        left_child_idx = MaxHeap.left_child_idx(idx)
        right_child_idx = MaxHeap.right_child_idx(idx)

        if left_child_idx < len(max_heap.heap_list):
            left_child = max_heap.heap_list[left_child_idx]
            if element < left_child:
                is_max_heap = False
                break

        if right_child_idx < len(max_heap.heap_list):
            right_child = max_heap.heap_list[right_child_idx]
            if element < right_child:
                is_max_heap = False
                break

    if is_max_heap:
        print("\nMaxHeap property holds: Passed")
    else:
        print("\nMaxHeap property holds: Failed")
        print("MaxHeap:", max_heap.heap_list)

    print()


def test_graph_find_path():
    print("Testing Graph find_path()...")

    # Create a new Graph instance
    railway = Graph()

    # Create vertices
    callan = Vertex('callan')
    peel = Vertex('peel')
    ulfstead = Vertex('ulfstead')
    harwick = Vertex('harwick')

    # Add vertices to the graph
    railway.add_vertex(callan)
    railway.add_vertex(peel)
    railway.add_vertex(harwick)
    railway.add_vertex(ulfstead)

    # Add edges between vertices
    railway.add_edge(peel, harwick)
    railway.add_edge(harwick, callan)
    railway.add_edge(callan, peel)

    # Test find_path() method
    peel_to_ulfstead_path_exists = railway.find_path('peel', 'ulfstead')
    harwick_to_peel_path_exists = railway.find_path('harwick', 'peel')

    # Check if the path exists
    if not peel_to_ulfstead_path_exists:
        print("\nNo path exists between peel and ulfstead: Passed")
    else:
        print("\nNo path exists between peel and ulfstead: Failed")

    if harwick_to_peel_path_exists:
        print("\nA path exists between harwick and peel: Passed")
    else:
        print("\nA path exists between harwick and peel: Failed")

    print()


def main():
    test_doubly_linked_list()
    test_stack()
    test_queue()
    test_hash_map()
    test_binary_search_tree()
    test_max_heap()
    test_max_heap_random_input()
    test_graph_find_path()


if __name__ == '__main__':
    main()
