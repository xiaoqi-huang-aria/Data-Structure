from SingleLL import SingleLinkedList
from DoubleLL import DoubleLinkedList
from Stack import Stack
from Queue import Queue

def testSLL():
    import random
    print("--------------------------------------------------------")
    print("             TEST - SINGLE LINKED LIST")
    print("--------------------------------------------------------")
    test_list = SingleLinkedList()
    for i in range(8):
        test_list.insert_from_head(random.randint(0, 20))
    print("Test list length 8, looks like:")
    print(test_list)
    print("--------------------------------------------------------")
    print("Maximum value within test list:", test_list.return_max())
    print("--------------------------------------------------------")
    print()
    print("--------------------------------------------------------")
    print("Testing insert_after_kth_position ............")
    test_list.insert_after_kth_index(0, "Hi")
    print(test_list)
    print("--------------------------------------------------------")


def testDLL():
    import random
    print("--------------------------------------------------------")
    print("             TEST - DOUBLE LINKED LIST")
    print("--------------------------------------------------------")
    test_list = DoubleLinkedList()
    for i in range(8):
        test_list.add_first(random.randint(0, 20))
    print("Test list length 8, looks like:")
    print(test_list)


def testStack():
    print("--------------------------------------------------------")
    print("             TEST - STACK")
    print("--------------------------------------------------------")
    mystack = Stack()
    print(mystack)
    mystack.push(8)
    mystack.push(5)
    print(mystack)
    print(mystack.peek())
    print(mystack.pop())
    print(mystack.pop())
    print(mystack.pop())
    print(mystack)


def testQueue():
    print("--------------------------------------------------------")
    print("             TEST - QUEUE")
    print("--------------------------------------------------------")
    myqueue = Queue()
    print(myqueue)
    myqueue.enqueue(8)
    myqueue.enqueue(5)
    print(myqueue)
    print(myqueue.peek())
    print(myqueue.dequeue())
    print(myqueue.dequeue())
    print(myqueue.dequeue())
    print(myqueue)

def main():
    testSLL()
    testDLL()
    testStack()
    testQueue()

main()


