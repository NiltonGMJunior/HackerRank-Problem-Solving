#!/bin/python3

import os
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def compare_lists(llist1, llist2):
    # If both heads are null, returns 1
    if (llist1 is None) and (llist2 is None):
        return 1
    
    # If only one of the heads is null, returns 0
    if (llist1 is None) or (llist2 is None):
        return 0
    
    cur1 = llist1
    cur2 = llist2

    # If heads are different returns 0 
    if cur1.data != cur2.data:
        return  0

    # While both nodes have a successor, checks to see if the successors are the same, return 0 otherwise
    while (cur1.next) and (cur2.next):
        if cur1.next.data == cur2.next.data:
            cur1 = cur1.next
            cur2 = cur2.next
        else:
            return 0
    
    # When either of the nodes is a tail, checks if both are tails, otherwise returns 0
    if (cur1.next) or (cur2.next):
        return 0

    # If all previous criteria is met, returns 1
    return 1
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()
