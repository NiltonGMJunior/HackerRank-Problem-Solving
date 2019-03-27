#!/bin/python3

import math
import os
import random
import re
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


def getNode(head, positionFromTail):

    
    # My solution is as follows:
    # An array is created containing all of the data in the linked list
    # We then count backwards from the array to find the desired data
      
    if head is None:
        return None
    
    llist_data = []
    cur = head
    while cur:
        llist_data.append(cur.data)
        cur = cur.next
    
    return llist_data[-1 - positionFromTail]
    
    # A better solution is as follows:
    # Two pointers are created pointing to the head of the list
    # One of the pointers moves along the list exactly n nodes, where n is the desidered position from the tail
    # When that pointer reaches a valid node, the other pointer starts pointing to the same node and the iteration repeats
    # When the first pointer reaches the end of the list, the second pointer will be pointing at the desired node

    # TODO: Implement this alternative solution
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        position = int(input())

        result = getNode(llist.head, position)

        fptr.write(str(result) + '\n')

    fptr.close()
